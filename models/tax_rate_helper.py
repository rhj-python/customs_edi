# coding:utf-8
from decimal import Decimal

from flask import g

from exts import db,app
from models.common_models import (Import_Customs_Declaration,
Export_Customs_Declaration,Tax_Rate,Commodity,Currency
)


class Tax_Calculator(object):
    trade_dic={'import_trade':'import_tax_rate','export_trade':'export_tax_rate'}

    @classmethod
    def tax_rate(cls,model,trade_type):
        tax_models = Tax_Rate.query.all()
        tax_mode = cls.trade_dic.get(trade_type)
        hs_code = model.hs_code
        tax_model = filter(lambda tax_model: tax_model.hs_code <= hs_code, tax_models)[-1]
        tax_rate = getattr(tax_model, tax_mode)
        return Decimal(tax_rate)

    @classmethod
    def calculator(cls,model,trade_type):
        tax_rate=cls.tax_rate(model,trade_type)
        exchange_rate=model.currency.exchange_rate

        # 总价*税率*汇率
        return model.total_price*tax_rate*exchange_rate

if __name__=='__main__':
    pass