# coding:utf-8
from datetime import datetime

from wtforms import (StringField,
IntegerField,BooleanField,DateTimeField)
from wtforms.validators import (URL,
Length,EqualTo,InputRequired,Regexp,Email)

from base_forms import BaseForm
from utils.rhjredis import Utils_Redis
from models.customs_models import Triple_Agreement
from exts import db

class GraphCaptchaForm(BaseForm):
    graph_captcha=StringField(validators=[Length(4,4,message=u'图片验证码长度为4位'),InputRequired(message=u'请输入图形验证码!')])

    def validate_graph_captcha(self,field):
        graph_captcha=field.data
        cache_graph_captcha=Utils_Redis.get(graph_captcha.lower())
        print cache_graph_captcha
        if not cache_graph_captcha or cache_graph_captcha!=graph_captcha.lower():
            self.graph_captcha.errors.append(u'验证码输入有误!')
            return False
        else:
            Utils_Redis.delete(graph_captcha.lower())
            return True


class AddTripleAgreementForm(BaseForm):
    company_uuid=StringField(validators=[InputRequired(message=u'必须制定企业ID')])
    agree=IntegerField(validators=[InputRequired(u'必须同意协议才能签约!')])


class CancelTripleAgreementForm(BaseForm):
    agreement_id=IntegerField(validators=[InputRequired(message=u'必须制定协议ID')])

    def validate_agreement_id(self,field):
        agreement_id=field.data

        agreement=Triple_Agreement.query.filter_by(id=agreement_id).first()
        if not agreement:
            self.agreement_id.errors.append(u'没有找到该协议!')
            return False
        elif agreement.status_id!=1:
            self.agreement_id.errors.append(u'行为状态不正确!')
            return False
        elif agreement.status_id==1:
            agreement.status_id=3
            agreement.reply_id=3
            agreement.cancel_time=datetime.now()
            agreement.cancel_name=agreement.company.legal_name
            db.session.commit()
            return True

