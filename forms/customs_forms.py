# coding:utf-8
from datetime import datetime,timedelta,date
import json

from wtforms import (StringField,
IntegerField,BooleanField,DateTimeField,
DecimalField,DateField)
from wtforms.validators import (URL,
Length,EqualTo,InputRequired,Regexp,Email)
from flask import session,request
from werkzeug.datastructures import ImmutableMultiDict

from base_forms import BaseForm,DeclarationBaseForm
from common_forms import GraphCaptchaForm
from utils.rhjredis import Utils_Redis
from models.customs_models import (Customs_User,
Customs_Zone,Employee,Triple_Status,Triple_Agreement,
Customs_Zone_Reply)
from models.common_models import (Import_Proxy_Agreement,
Export_Proxy_Agreement,Proxy,Pay_Mode,Transaction_Mode,
Trade_Mode,Agreement_Status,Tax_Mode,Use,Transport_Mode,
Currency,Tax_Free_Mode,Document,Document_Type,Import_Customs_Declaration,
Settlement_Mode,Export_Customs_Declaration)

from constants import CUSTOMS_SESSION_ID,EMPLOYEE_SESSION_ID,DELAY_CHECK_DAYS
from exts import db
from models.tax_rate_helper import Tax_Calculator



class CustomsLoginForm(GraphCaptchaForm):
    username=StringField(validators=[InputRequired(message=u'请输入用户名!'),Length(3,12,message=u'用户名或密码错误!')])
    password=StringField(validators=[InputRequired(message=u'请输入密码!'),Length(6,20,message='用户名或密码输入有误!')])
    remember=IntegerField()

    def validate(self):
        if not super(CustomsLoginForm,self).validate():
            return False
        else:
            username=self.username.data
            password=self.password.data
            remember=self.remember.data

            user=Customs_User.query.filter_by(username=username).first()
            if not user or not user.check_pwd(password):
                self.username.errors.append(u'用户名或密码错误!')
                return False
            elif not user.is_active:
                self.username.errors.append(u'该帐号已被封锁,请联系管理员!')
                return False
            else:
                session[CUSTOMS_SESSION_ID]=user.id
                if remember:
                    session.permanent=True
                return True

class CustomsAddZoneForm(BaseForm):
    name=StringField(validators=[InputRequired(message=u'请输入关区名称!')])

    def validate(self):
        if not super(CustomsAddZoneForm, self).validate():
            return False
        else:
            name=self.name.data
            db_zone=Customs_Zone.query.filter_by(name=name).first()
            if db_zone:
                self.name.errors.append('该关区已存在,不能重复添加!')
                return False
            else:
                zone=Customs_Zone(name=name)
                db.session.add(zone)
                db.session.commit()
            return True

class CustomsEditZoneForm(BaseForm):
    id=IntegerField(validators=[InputRequired(message=u'必须指定关区ID')])
    name=StringField(validators=[InputRequired(message=u'请输入关区名称!')])

    def validate(self):
        if not super(CustomsEditZoneForm, self).validate():
            return False
        else:
            id=self.id.data
            name=self.name.data
            zone=Customs_Zone.query.filter_by(id=id).first()
            db_zone=Customs_Zone.query.filter_by(name=name).first()

            if not zone:
                self.id.errors.append(u'没有找到该关区!')
                return False
            elif db_zone:
                self.name.errors.append(u'该关区已存在，请重命名该关区!')
                return False
            else:
                zone.name=name
                db.session.commit()
                return True

class CustomsDeleteZoneForm(BaseForm):
    id=IntegerField(validators=[InputRequired(message=u'必须指定关区ID')])

    def validate(self):
        if not super(CustomsDeleteZoneForm, self).validate():
            return False
        else:
            id=self.id.data
            zone=Customs_Zone.query.filter_by(id=id).first()
            if not zone:
                self.id.errors.append(u'没有找到该关区!')
                return False
            elif zone.agreements:
                self.id.errors.append(u'该关区下还有与企业签订的三方协议,请全部解约完再删除!')
                return False
            else:
                db.session.delete(zone)
                db.session.commit()
                return True


class CustomsEmployeeLoginForm(CustomsLoginForm):
    def validate(self):
        if not super(CustomsLoginForm,self).validate():
            return False
        else:
            username=self.username.data
            password=self.password.data
            remember=self.remember.data

            user=Employee.query.filter_by(username=username).first()
            if not user or not user.check_pwd(password):
                self.username.errors.append(u'用户名或密码错误!')
                return False

            elif not user.is_active:
                self.username.errors.append(u'该帐号已被封锁,请联系管理员!')
                return False

            else:
                session[EMPLOYEE_SESSION_ID]=user.id
                if remember:
                    session.permanent=True
                return True


class AgreementApprovalSuccessForm(BaseForm):
    agreement_id=IntegerField(validators=[InputRequired(message=u'必须指定协议ID')])

    def validate_agreement_id(self,field):
        agreement_id=field.data

        agreement=Triple_Agreement.query.filter_by(id=agreement_id).first()
        if not agreement:
            self.agreement_id.errors.append(u'没有找到该协议!')
            return False
        else:
            agreement.status_id=1
            agreement.reply_id=1
            agreement.sign_name = agreement.company.legal_name
            agreement.cancel_name=None
            agreement.cancel_time=None
            db.session.commit()
            return True

class AgreementApprovalFailForm(BaseForm):
    agreement_id=IntegerField(validators=[InputRequired(message=u'必须输入协议ID')])
    reply_id=IntegerField(validators=[InputRequired(message=u'请指定审核未通过原因')])

    def validate(self):
        if not super(AgreementApprovalFailForm, self).validate():
            return False
        else:
            agreement_id=self.agreement_id.data
            reply_id=self.reply_id.data

            agreement=Triple_Agreement.query.filter_by(id=agreement_id).first()
            reply=Customs_Zone_Reply.query.filter_by(id=reply_id).first()

            if not agreement:
                self.agreement_id.errors.append(u'没有找到该协议!')
                return False
            elif not reply:
                self.reply_id.errors.append(u'没有找到该原因!')
            else:
                agreement.reply=reply
                agreement.status_id=4
                db.session.commit()
                return True

class CustomsAddProxyAgreementForm(BaseForm):
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
        if not super(CustomsAddProxyAgreementForm,self).validate():
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
            status=Agreement_Status.query.filter_by(id=1).first()
            agreement.status=status


            db.session.add(agreement)
            db.session.commit()
            return True

class CUstomsDeclarationBase(BaseForm):
    pre_entry_code=StringField(validators=[Length(12,12,message=u'预录入编号长度为12位!'),InputRequired(message=u'预录入号不能为空')])
    agreement_id=IntegerField(validators=[InputRequired(message=u'预录入号不能为空!')])
    customs_date=DateField(validators=[InputRequired(message=u'请指定申报日期')])
    case_code=StringField()
    contract_code=StringField(validators=[InputRequired(message=u'请输入合同协议号!')])
    consignee=StringField(validators=[InputRequired(message=u'请输入收货人名称!')])
    transport_mode_id=IntegerField(validators=[InputRequired(message=u'请选择运输方式')])
    vessel_name=StringField()
    vessel_code=StringField()
    bl_code=StringField(validators=[InputRequired(message=u'请输入提单号!')])
    trade_mode_id=IntegerField(validators=[InputRequired(message=u'请选择贸易方式!')])
    tax_mode_id=IntegerField(validators=[InputRequired(message=u'请选择征免性质!')])
    tax_rate=StringField()
    license_code=StringField()
    approval_code=StringField()
    transaction_mode_id=IntegerField(validators=[InputRequired(message=u'请选择成交方式!')])
    freight=StringField()
    insurance_premiums=StringField()
    sundry_charges=StringField()
    packages_num=IntegerField(validators=[InputRequired(message=u'请输入包装数量')])
    packing_type=StringField(validators=[InputRequired(message=u'请输入包装种类!')])
    gross_weight=DecimalField(validators=[InputRequired(message=u'请输入毛重!')])
    net_weight=DecimalField(validators=[InputRequired(message=u'请输入毛重!')])
    container_code=StringField()
    marks=StringField()

    def validate(self):
        if not super(CUstomsDeclarationBase, self).validate():
            return False
        else:
            agreement_id = self.agreement_id.data
            transport_mode_id = self.transport_mode_id.data
            trade_mode_id = self.trade_mode_id.data
            tax_mode_id = self.tax_mode_id.data
            transaction_mode_id = self.transaction_mode_id.data

            foreign_dic=dict(
                agreement = Import_Proxy_Agreement.query.filter_by(id=agreement_id).first(),
                transport_mode = Transport_Mode.query.filter_by(id=transport_mode_id).first(),
                trade_mode = Trade_Mode.query.filter_by(id=trade_mode_id).first(),
                tax_mode = Tax_Mode.query.filter_by(id=tax_mode_id).first(),
                transaction_mode = Transaction_Mode.query.filter_by(id=transaction_mode_id).first(),
            )
            message_dic=dict(agreement=u'没有找到该委托协议!',transport_mode=u'没有找到该运输方式!',trade_mode=u'没有找到该贸易方式!',
                     tax_mode=u'没有找到该征免性质',transaction_mode=u'没有找到该成交方式')

            for k,v in foreign_dic.iteritems():
                if not v:
                    message=message_dic.get(k)
                    try:
                        getattr(self,k+'_id').errors.append(message=message)
                        return False
                    except Exception as e:
                        print e
                        print 'foreign key error'

            return True

class AddCommodityForm(BaseForm):
    item_code=StringField(validators=[InputRequired(message=u'请输入项号')])
    hs_code=StringField(validators=[InputRequired(message=u'请输入商品编码!'),Length(10,10,message=u'商品编码长度为10位!')])
    commodity_name=StringField(validators=[InputRequired(message=u'请输入商品名称!')])
    commodity_type=StringField(validators=[InputRequired(message=u'请输入商品规格型号!')])
    quantity_and_unit=StringField(validators=[InputRequired(message=u'请输入数量和单位')])
    unit_price=DecimalField(validators=[InputRequired(message=u'请输入单价!')])
    total_price=DecimalField(validators=[InputRequired(message=u'请输入总价!')])
    currency_id=IntegerField(validators=[InputRequired(message=u'请选择币制!')])
    tax_free_mode_id=IntegerField(validators=[InputRequired(message=u'请选择征免!')])

    def validate(self):
        if not super(AddCommodityForm, self).validate():
            return False
        else:
            currency_id=self.currency_id.data
            tax_free_mode_id=self.tax_free_mode_id.data

            currency=Currency.query.filter_by(id=currency_id).first()
            tax_free_mode=Tax_Free_Mode.query.filter_by(id=tax_free_mode_id).first()

            if not currency:
                self.currency_id.errors.append(u'没有找到该币制')
                return False

            elif not tax_free_mode:
                self.tax_free_mode_id.errors.append(u'没有找到该币制')
                return False

            else:
                return True

class AddDocumentForm(BaseForm):
    document_type_id=IntegerField(validators=[InputRequired(message=u'请选择单据类型!')])
    name=StringField(validators=[InputRequired(message=u'请输入单据名称!')])
    url=StringField(validators=[URL(message=u'您的单据文件有误!'),InputRequired(message=u'请上传您的单据文件!')])

    def validate(self):
        if not super(AddDocumentForm, self).validate():
            return False
        else:
            document_type_id=self.document_type_id.data
            document_type=Document_Type.query.filter_by(id=document_type_id).first()

            if not document_type:
                self.document_type_id.errors.append(u'没有找到该单据类型!')
                return False
            else:
                return True


class ImportCustomsDeclarationForm(CUstomsDeclarationBase):
    import_port=StringField(validators=[InputRequired(message=u'请输入进口口岸!')])
    import_date=DateField(validators=[InputRequired(message=u'请指定进口日期!')])
    departure_country=StringField(validators=[InputRequired(message=u'请输入起运国!')])
    loading_port=StringField(validators=[InputRequired(message=u'请输入装货港名称!')])
    domestic_destination=StringField(validators=[InputRequired(message=u'请输入境内目的地!')])
    use_id=IntegerField(validators=[InputRequired(message=u'请选择用途!')])

    def validate(self):
        if not super(ImportCustomsDeclarationForm, self).validate():
            return False
        else:
            use_id = self.use_id.data
            use = Use.query.filter_by(id=use_id).first()
            import_port=self.import_port.data
            agreement_id=self.agreement_id.data

            agreement=Import_Proxy_Agreement.query.filter_by(id=agreement_id).first()
            zone=Customs_Zone.query.filter_by(name=import_port).first()

            client_triple_agreements=agreement.proxy.client.agreements
            broker_triple_agreements=agreement.proxy.broker.agreements

            client_has_agreement=filter(lambda agreement:(zone.id==agreement.zone_id and agreement.status_id==1),client_triple_agreements) if zone else None
            broker_has_agreement=filter(lambda agreement:(zone.id==agreement.zone_id and agreement.status_id==1),broker_triple_agreements) if zone else None

            commodity_li=request.form.getlist('commodity_li[]')
            document_li=request.form.getlist('document_li[]')

            if not zone:
                self.import_port.errors.append(u'没有找到该海关!')
                return False

            elif not client_has_agreement:
                self.import_port.errors.append(u'经营单位签订三方协议!')
                return False

            elif not broker_has_agreement:
                self.import_port.errors.append(u'申报单位签订三方协议!')
                return False

            elif not use:
                self.use_id.errors.append(u'没有找到该用途!')
                return False

            elif not commodity_li:
                self.import_port.errors.append(u'请至少指定一项商品!')
                return False
            elif not document_li:
                self.import_port.errors.append(u'请上传随附单据!!')
                return False

            else:
                for commodity in commodity_li:
                    commodity=json.loads(commodity)
                    c_form=AddCommodityForm(ImmutableMultiDict(commodity.items()))
                    if  not c_form.validate():
                        self.import_port.errors.append(c_form.get_error())
                        return False

                for document in document_li:
                    document=json.loads(document)
                    d_form=AddDocumentForm(ImmutableMultiDict(document.items()))
                    if  not d_form.validate():
                        self.import_port.errors.append(d_form.get_error())
                        return False

                return True


class ExportCustomsDeclarationForm(CUstomsDeclarationBase):
    export_port=StringField(validators=[InputRequired(message=u'请输入出口口岸!')])
    export_date=DateField(validators=[InputRequired(message=u'请指定出口日期!')])
    destination_country=StringField(validators=[InputRequired(message=u'请输入运抵国!')])
    destination_port=StringField(validators=[InputRequired(message=u'请输入装目的港名称!')])
    goods_origin_place=StringField(validators=[InputRequired(message=u'请输入货源地')])
    manufacturer=StringField(validators=[InputRequired(message=u'请输入生产厂家!')])
    settlement_mode_id=IntegerField(validators=[InputRequired(message=u'请选择结汇方式!')])

    def validate(self):
        if not super(ExportCustomsDeclarationForm, self).validate():
            return False
        else:
            settlement_mode_id = self.settlement_mode_id.data
            settlement_mode = Settlement_Mode.query.filter_by(id=settlement_mode_id).first()
            export_port=self.export_port.data
            agreement_id=self.agreement_id.data

            agreement=Export_Proxy_Agreement.query.filter_by(id=agreement_id).first()
            zone=Customs_Zone.query.filter_by(name=export_port).first()

            client_triple_agreements=agreement.proxy.client.agreements
            broker_triple_agreements=agreement.proxy.broker.agreements

            client_has_agreement=filter(lambda agreement:(zone.id==agreement.zone_id and agreement.status_id==1),client_triple_agreements) if zone else None
            broker_has_agreement=filter(lambda agreement:(zone.id==agreement.zone_id and agreement.status_id==1),broker_triple_agreements) if zone else None

            commodity_li=request.form.getlist('commodity_li[]')
            document_li=request.form.getlist('document_li[]')

            if not zone:
                self.export_port.errors.append(u'没有找到该海关!')
                return False

            elif not client_has_agreement:
                self.export_port.errors.append(u'经营单位签订三方协议!')
                return False

            elif not broker_has_agreement:
                self.export_port.errors.append(u'申报单位签订三方协议!')
                return False

            elif not settlement_mode:
                self.settlement_mode_id.errors.append(u'没有找到该用途!')
                return False

            elif not commodity_li:
                self.export_port.errors.append(u'请至少指定一项商品!')
                return False
            elif not document_li:
                self.export_port.errors.append(u'请上传随附单据!!')
                return False

            else:
                for commodity in commodity_li:
                    commodity=json.loads(commodity)
                    c_form=AddCommodityForm(ImmutableMultiDict(commodity.items()))
                    if  not c_form.validate():
                        self.export_port.errors.append(c_form.get_error())
                        return False

                for document in document_li:
                    document=json.loads(document)
                    d_form=AddDocumentForm(ImmutableMultiDict(document.items()))
                    if  not d_form.validate():
                        self.export_port.errors.append(d_form.get_error())
                        return False

                return True

class EditImportDeclarationForm(ImportCustomsDeclarationForm):
    declaration_uuid=StringField(validators=[InputRequired(message=u'请指定报关单的uuid!')])

class EditExportDeclarationForm(ExportCustomsDeclarationForm):
    declaration_uuid=StringField(validators=[InputRequired(message=u'请指定报关单的uuid!')])





class CollectTaxForm(DeclarationBaseForm):
    def validate(self):
        if not super(CollectTaxForm, self).validate():
            return False
        else:

            if self.declaration.status_id==2:
                tax_price=0
                for commodity in self.declaration.commoditys:
                    tax_price += Tax_Calculator.calculator(commodity, 'import_trade')
                self.declaration.status_id=4
                self.declaration.tax_price=tax_price

                db.session.commit()
                return True
            else:
                self.declaration_uuid.errors.append(u'操作行为有误!')
                return False

class CheckForm(DeclarationBaseForm):
    def validate(self):
        if not super(CheckForm, self).validate():
            return False
        else:
            if self.declaration.status_id == 2:
                self.declaration.status_id=3
                self.declaration.check_date=datetime.now()+timedelta(days=DELAY_CHECK_DAYS)
                db.session.commit()
                return True
            else:
                self.declaration_uuid.errors.append(u'操作行为有误!')
                return False

class RefundForm(DeclarationBaseForm):
    refund_reason=StringField(validators=[InputRequired(message=u'请输入退单原因!')])

    def validate(self):
        if not super(RefundForm,self).validate():
            return False
        else:
            refund_reason=self.refund_reason.data

            if self.declaration.status_id in [2,3]:
                self.declaration.refund_reason=refund_reason
                self.declaration.status_id=5
                db.session.commit()
                return True

            else:
                self.declaration_uuid.errors.append(u'操作行为有误!')
                return False

class CheckSuccessForm(DeclarationBaseForm):
    def validate(self):
        if not super(CheckSuccessForm, self).validate():
            return False
        else:
            if self.declaration.status_id==3:
                self.declaration.status_id=4
                db.session.commit()
                return True
            else:
                self.declaration_uuid.errors.append(u'操作行为有误!')
                return False