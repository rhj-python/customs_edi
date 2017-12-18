# coding:utf-8
from datetime import timedelta

from flask import session,request
from wtforms import StringField,IntegerField,BooleanField,DecimalField,DateField,DateTimeField
from wtforms.validators import Length,EqualTo,NumberRange,InputRequired,Email,Regexp

from forms.base_forms import BaseForm,DeclarationBaseForm
from utils.rhjredis import Utils_Redis
from utils.captcha.xtcaptcha import Captcha
from tasks import celery_send_sms
from constants import SMS_TIME,FRONT_SESSION_ID
from forms.common_forms import GraphCaptchaForm
from models.common_models import (Company,Proxy,Import_Proxy_Agreement,
Export_Proxy_Agreement,Pay_Mode,Trade_Mode,Business_Content,Agreement_Status)
from models.front_models import Front_User
from exts import db
from constants import EXPIRE_TIME


class SMSCaptchaForm(BaseForm):
    phone=StringField(validators=[Length(11,11,message=u'手机号格式有误'),InputRequired(message=u'请输入手机号!')])

    def validate(self):
        if not super(SMSCaptchaForm,self).validate():
            return False
        else:
            phone=self.phone.data

            db_cache=Utils_Redis.get(phone)

            Captcha.number=6
            text=Captcha.gene_text()
            Captcha.number = 4


            if db_cache:
                self.phone.errors.append(u'已经向该手机发送验证码了,请%s分钟后再试!' %SMS_TIME)
                return False

            else:
                Utils_Redis.set(phone,text.lower(),ex=SMS_TIME*60)
                celery_send_sms.delay(phone,text)
                return True

class FrontRegistForm(GraphCaptchaForm):
    phone=StringField(validators=[Length(11,11,message=u'手机号格式有误!'),InputRequired(message=u'请输入手机号')])
    sms_captcha=StringField(validators=[Length(6,6,message=u'短息验证码长度不正确!'),InputRequired(message=u'请输入短信验证码!')])
    username=StringField(validators=[Length(3,12,message=u'用户名长度在3-12位之间!'),InputRequired(message=u'请输入用户名')])
    password=StringField(validators=[Length(6,20,message=u'密码长度在6-20位之间'),InputRequired(message=u'请输入密码')])
    password_repeat=StringField(validators=[EqualTo('password')])

    company_name=StringField(validators=[Length(5,100,message=u'企业名称长度在3-100字符之间'),InputRequired(message=u'请输入企业名称!')])
    company_address=StringField(validators=[Length(5,100,message=u'企业地址长度在3-100字符之间'),InputRequired(message=u'请输入公司地址!')])
    customs_registration_code=StringField(validators=[Length(10,10,message=u'海关注册号输入有误!'),InputRequired(message=u'请输入企业的海关注册号!')])
    organization_code=StringField(validators=[Length(9,9,message=u'组织机构代码输入有误!'),InputRequired(message=u'请输入组织机构代码!')])
    legal_name=StringField(validators=[Length(2,10,message=u'企业法人名称长度在3-10位之间!'),InputRequired(message=u'请输入企业法人名称!')])


    def validate(self):
        if not super(FrontRegistForm,self).validate():
            return False
        else:
            phone = self.phone.data
            sms_captcha = self.sms_captcha.data
            username = self.username.data
            password = self.password.data

            company_name = self.company_name.data
            company_address = self.company_address.data
            customs_registration_code = self.customs_registration_code.data
            organization_code = self.organization_code.data
            legal_name = self.legal_name.data

            cache_sms_captcha=Utils_Redis.get(phone)
            db_user=Front_User.query.filter_by(phone=phone).first()
            db_company=Company.query.filter_by(organization_code=organization_code).first()

            if not cache_sms_captcha or sms_captcha.lower()!=cache_sms_captcha.lower():
                self.sms_captcha.errors.append(u'短信验证码输入有误!')
                return False

            elif db_user:
                self.phone.errors.append(u'该用户已注册!')
                return False

            else:
                user=Front_User(phone=phone,username=username,password=password)
                if not db_company:
                    company=Company(company_name=company_name,company_address=company_address,
                                    customs_registration_code=customs_registration_code,organization_code=organization_code,
                                    legal_name=legal_name)
                    company.users.append(user)
                    db.session.add(company)
                    db.session.commit()
                else:
                    db_company.users.append(user)
                    db.session.commit()
                return True

class FrontLoginForm(GraphCaptchaForm):
    phone = StringField(validators=[Length(11, 11, message=u'手机号格式有误!'), InputRequired(message=u'请输入手机号')])
    password=StringField(validators=[Length(6,20,message=u'密码长度在6-20位之间'),InputRequired(message=u'请输入密码')])
    remember=IntegerField()

    def validate(self):

        if not super(FrontLoginForm, self).validate():
            return False
        else:
            phone=self.phone.data
            password=self.password.data
            remember=self.remember.data

            user=Front_User.query.filter_by(phone=phone).first()
            if not user or not user.check_pwd(password):
                self.password.errors.append(u'帐号或密码错误!')
                return False

            elif not user.is_active:
                self.phone.errors.append(u'该帐号已被封锁,请联系管理员!')
                return False

            else:
                session[FRONT_SESSION_ID]=user.id
                if remember:
                    session.permanent=True
                return True


class AddProxyAgreementForm(BaseForm):
    proxy_id=IntegerField(validators=[InputRequired(message=u'必须指定委托书ID!')])
    trade_class=IntegerField(validators=[InputRequired(message=u'请选择贸易种类!')])
    goods_name=StringField(validators=[Length(2,60,message=u'主要货物名称长度在3-60位!'),InputRequired(message=u'请输入货物名称!')])
    hs_code=StringField(validators=[Length(10,10,message=u'HS编码长度为10位'),InputRequired(message=u'请输入HS编码')])
    total_price=DecimalField(validators=[InputRequired(message=u'请输入货物总价')])
    customs_price=IntegerField()
    import_or_export_date=DateField(validators=[InputRequired(message=u'请输入进出口日期!')])
    bl_code=StringField(validators=[Length(max=100,message=u'提货单格式输入有误!'),InputRequired(message=u'请输入提货单号!')])
    trade_mode_id=IntegerField(validators=[InputRequired(message=u'请选择贸易方式!')])
    country=StringField(validators=[InputRequired(message=u'请输入原产国或运抵国!')])
    other=StringField()
    telephone=StringField(validators=[Length(max=100,message=u'联系电话格式有误!')])
    pay_mode_id=IntegerField(validators=[InputRequired(message=u'请选择付款方!')])

    def validate(self):
        if not super(AddProxyAgreementForm,self).validate():
            return False

        proxy_id=self.proxy_id.data
        trade_class=self.trade_class.data

        goods_name=self.goods_name.data
        hs_code=self.hs_code.data
        total_price=self.total_price.data
        import_or_export_date=self.import_or_export_date.data
        bl_code=self.bl_code.data
        trade_mode_id=self.trade_mode_id.data
        country=self.country.data

        pay_mode_id=self.pay_mode_id.data


        customs_price = self.customs_price.data if self.telephone.data else 0
        telephone = self.telephone.data if self.telephone.data else None
        other = self.other.data if self.telephone.data else None

        proxy=Proxy.query.filter_by(id=proxy_id).first()
        pay_mode=Pay_Mode.query.filter_by(id=pay_mode_id).first()
        trade_mode=Trade_Mode.query.filter_by(id=trade_mode_id).first()

        if not proxy_id:
            self.proxy_id.errors.append(u'没有找到该委托书')
            return False
        elif not pay_mode:
            self.pay_mode_id.errors.append(u'没有找到该付款方！')
            return False

        elif not trade_mode:
            self.trade_mode_id.errors.append(u'没有找到该贸易方式！')
            return False

        else:
            agreement=None
            if trade_class==1:
                agreement=Import_Proxy_Agreement(goods_name=goods_name,
                hs_code=hs_code,total_price=total_price,
                import_or_export_date=import_or_export_date,
                bl_code=bl_code,origin_country=country,
                )

            elif trade_class==2:
                agreement = Export_Proxy_Agreement(goods_name=goods_name,
                hs_code=hs_code, total_price=total_price,
                import_or_export_date=import_or_export_date,
                bl_code=bl_code, destination_country=country,
                )


            agreement.telephone=telephone
            agreement.customs_price=customs_price
            agreement.other=other
            agreement.pay_mode=pay_mode
            agreement.trade_mode=trade_mode
            agreement.proxy=proxy
            status=Agreement_Status.query.filter_by(id=2).first()
            agreement.status=status


            db.session.add(agreement)
            db.session.commit()
            return True

class AddProxyForm(BaseForm):
    proxy_id=IntegerField(InputRequired(message=u'必须指定委托书ID!'))
    expiry_time_id=IntegerField(InputRequired(message=u'请选择委托书的有效期!'))

    def validate(self):
        if not super(AddProxyForm, self).validate():
            return False
        else:
            proxy_id=self.proxy_id.data
            expiry_time_id=self.expiry_time_id.data
            content_li=request.form.getlist('content_li[]')

            proxy=Proxy.query.filter_by(id=proxy_id).first()
            expiry_time=EXPIRE_TIME.get(expiry_time_id)

            if not proxy:
                self.proxy_id.errors.append(u'没有找到该委托书!')
                return False

            elif not expiry_time:
                self.expiry_time_id.errors.append(u'没有找到有效期限!')
                return False

            else:
                proxy.expiry_time=proxy.create_time+timedelta(days=expiry_time)
                for content_id in content_li:
                    content=Business_Content.query.filter_by(id=content_id).first()
                    if content:
                        proxy.contents.append(content)
                db.session.commit()
                return True

class CancelProxyFrom(BaseForm):
    proxy_id=IntegerField(validators=[InputRequired(message=u'必须指定委托书ID')])

    def validate_proxy_id(self,field):
        proxy_id=field.data

        proxy=Proxy.query.filter_by(id=proxy_id).first()

        if not proxy:
            self.proxy_id.errors.append(u'没有找到该委托书!')
            return False
        else:
            if proxy.import_agreements:
                for im_agreement in proxy.import_agreements:
                    db.session.delete(im_agreement)
            if proxy.export_agreements:
                for ex_agreement in proxy.export_agreements:
                    db.session.delete(ex_agreement)

            db.session.commit()
            return True

class OperateProxyAgreementForm(BaseForm):
    agreement_type_id=IntegerField(validators=[InputRequired(message=u'必须指定委托协议的类型ID')])
    agreement_id=IntegerField(validators=[InputRequired(message=u'必须指定委托协议ID')])
    operate_id=IntegerField(validators=[InputRequired(message=u'必须指定操作行为!')])
    status_id=IntegerField(validators=[InputRequired(message=u'必须指定协议状态')])

    def validate(self):
        if not super(OperateProxyAgreementForm, self).validate():
            return False
        else:
            agreement_type_id = self.agreement_type_id.data
            agreement_id = self.agreement_id.data
            operate_id = self.operate_id.data
            status_id = self.status_id.data

            want_status = Agreement_Status.query.filter_by(id=operate_id).first()
            now_status = Agreement_Status.query.filter_by(id=status_id).first()

            agreement = ''
            if not want_status or want_status.id not in[2,3]:
                self.operate_id.errors.append(u'操作行为有误!')
                return False
            if not now_status or now_status.id!=1:
                self.status_id.errors.append(u'委托协议状态不正确!')
                return False

            if agreement_type_id == 1:
                agreement = Import_Proxy_Agreement.query.filter_by(id=agreement_id).first()
            elif agreement_type_id == 2:
                agreement = Export_Proxy_Agreement.query.filter_by(id=agreement_id).first()
            else:
                self.agreement_type_id.errors.append(u'没有找到该委托协议类型!')
                return False

            if not agreement:
                self.agreement_id.errors.append(u'没有找到该协议!')
                return False

            else:
                agreement.status=want_status
                db.session.commit()
                return True


class FrontRefundReasonForm(DeclarationBaseForm):
    pass


class FrontPayTaxNowForm(DeclarationBaseForm):

    def validate(self):
        if not super(FrontPayTaxNowForm, self).validate():
            return False
        else:
            if self.declaration.status_id==4:
                self.declaration.status_id=6
                db.session.commit()
                return True
            else:
                self.declaration_uuid.errors.append(u'操作行为有误!')
                return False