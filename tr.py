# coding:utf-8
import datetime
import json

from wtforms import StringField,IntegerField,BooleanField,DecimalField
from wtforms.validators import Length,InputRequired,EqualTo,Email
from flask import request

from exts import app,db
from forms.common_forms import BaseForm
from werkzeug.datastructures import ImmutableMultiDict
from models.common_models import Import_Customs_Declaration

# a=datetime.datetime(2014,2,14,19,47,53)
# b=datetime.datetime(2014,2,14,22,47,53)
#
# print a+datetime.timedelta(days=90)

# a='[1,2,3]'
#
# print json.loads(a)

# class TForm(BaseForm):
#     username=StringField(validators=[Length(3,12)])
#     password=StringField(validators=[Length(6,12)])
#

# li=[('vessel_code', u''), ('packages_num', u'1'), ('document_li[0][document_name]', u'1'), ('sundry_charges', u''), ('consignee', u'1'), ('net_weight', u'1'), ('packing_type', u'1'), ('freight', u''), ('trade_mode_id', u'1'), ('import_port', u'1'), ('container_code', u''), ('tax_mode_id', u'1'), ('license_code', u''), ('insurance_premiums', u''), ('import_date', u'2017-11-14'), ('departure_country', u'\u7f8e\u56fd'), ('vessel_name', u'1'), ('marks', u''), ('bl_code', u'12345678'), ('commodity_li[0][unit_price]', u'1'), ('commodity_li[0][commodity_name]', u'\u4e2d\u534e\u50b2\u9f99\u87f9'), ('commodity_li[0][quantity_and_unit]', u'1'), ('transaction_mode_id', u'1'), ('customs_date', u'2017-11-14'), ('transport_mode_id', u'1'), ('loading_port', u'1'), ('tax_rate', u''), ('domestic_destination', u'1'), ('approval_code', u''), ('agreement_id', u'15'), ('case_code', u''), ('commodity_li[0][currency_id]', u'1'), ('commodity_li[0][total_price]', u'7680.00'), ('document_li[0][document_type_id]', u'1'), ('gross_weight', u'1'), ('commodity_li[0][item_code]', u'1'), ('commodity_li[0][hs_code]', u'1112223334'), ('contract_code', u'1'), ('use_id', u'1'), ('commodity_li[0][tax_free_mode_id]', u'1'), ('pre_entry_code', u'123456781234'), ('commodity_li[0][departure_country]', u'\u7f8e\u56fd')]


# declaration='Import_Customs_Declaration.query.filter_by(id=3).first()'
# print eval(declaration).declaration_code





