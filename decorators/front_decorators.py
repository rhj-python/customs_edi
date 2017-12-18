# coding:utf-8

from functools import wraps


from flask import (
session,redirect,url_for,request,abort,render_template
)


from constants import FRONT_SESSION_ID
from business_exts import trade_type_dic

def front_login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if not session.get(FRONT_SESSION_ID):
            return redirect(url_for('front_account.front_login',next=request.path))
        else:
            return func(*args,**kwargs)
    return wrapper


def front_trade_type(func):
    @wraps(func)
    def wrapper(declaration_uuid,*args,**kwargs):
        # declaration = Import_Customs_Declaration.query.filter_by(uuid=declaration_uuid).first()
        # context = dict(declaration=declaration)
        # if not declaration:
        #     abort(404)
        # else:
        #     return render_template('front/front_import_declaration_detail.html', **context)

        trade_type=func.__name__.split('_')[1]

        model=trade_type_dic.get(trade_type)
        declaration=model.query.filter_by(uuid=declaration_uuid).first()
        context=dict(declaration=declaration)
        if not declaration:
            abort(404)
        else:
            path='front/front_%s_declaration_detail.html' %trade_type
            return render_template(path,**context)
    return wrapper
