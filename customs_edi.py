 #coding:utf-8
from functools import wraps
from datetime import date,datetime

from flask import (Flask,request,
render_template,redirect,url_for,
session,g)

import flask
from flask_wtf import CSRFProtect


from exts import app,socketio
import exts
from views.customs_views import customs_views,customs_account_views,manage_views
from views.common_views import common_views
from views.front_views import front_views,front_account_views
from views.ws_views import ws_views
from views.chart_views import chart_views
from constants import CUSTOMS_SESSION_ID,EMPLOYEE_SESSION_ID,FRONT_SESSION_ID
from utils import xtjson
from models.customs_models import Customs_User,Employee
from models.front_models import Front_User
from models.tax_rate_helper import Tax_Calculator
from permissions.customs_permissions import Permission_Handler
from models.ws_model_helper import all_chat

# @app.route('/')
# def hello_world():
#     return 'Hello World!'



app.register_blueprint(exts.customs_bp)
app.register_blueprint(customs_account_views.bp)
app.register_blueprint(common_views.bp)

app.register_blueprint(front_views.bp)
app.register_blueprint(front_account_views.bp)
app.register_blueprint(ws_views.bp)
app.register_blueprint(chart_views.bp)


@app.before_request
def add_customs_user_to_g():
    user_id=session.get(CUSTOMS_SESSION_ID)
    if user_id:
        user=Customs_User.query.filter_by(id=user_id).first()
        if user:
            g.customs_user=user

@app.context_processor
def add_customs_user_to_template():
    if hasattr(g,'customs_user'):
        return dict(customs_user=g.customs_user)
    else:
        return {}

@app.before_request
def add_employee_to_g():
    user_id=session.get(EMPLOYEE_SESSION_ID)
    if user_id:
        user=Employee.query.filter_by(id=user_id).first()
        if user:
            g.employee=user

@app.context_processor
def add_employee_to_template():
    if hasattr(g,'employee'):
        return dict(employee=g.employee)
    else:
        return {}

@app.before_request
def add_front_user_to_g():
    id=session.get(FRONT_SESSION_ID)
    if id:
        user=Front_User.query.filter_by(id=id).first()
        if user:
            g.front_user=user

@app.context_processor
def add_g_to_template():
    if hasattr(g,'front_user'):
        return dict(front_user=g.front_user)
    else:
        return {}

@app.context_processor
def add_permission_to_template():
    return dict(has_permission=Permission_Handler.has_permission)

@app.context_processor
def add_all_broadcast_messages_to_template():
    msg_alls=all_chat()
    return dict(msg_alls=msg_alls)



@app.template_filter('date')
def to_date(value):
    if isinstance(value,(date,datetime)):
        return value.strftime('%Y-%m-%d')
    else:
        return value

@app.template_filter('datetime')
def to_datetime(value):
    if isinstance(value,datetime):
        return value.strftime('%Y-%m-%d %H:%M:%S',)
    else:
        return value

@app.template_filter('timeout')
def to_timeout(value):
    if isinstance(value,datetime):
        now=datetime.now()
        seconds=(value-now).total_seconds()
        return True if seconds<0 else False
    else:
        return value

@app.template_filter('tax_rate')
def model_to_tax_rate(value,trade_type='import_trade'):
    if value is not None:
        tax_rate=Tax_Calculator.tax_rate(value,trade_type)
        return tax_rate
    else:
        return value

@app.template_filter('tax_price')
def model_to_tax_price(value,trade_type='import_trade'):
    if value is not None:
        tax_price=Tax_Calculator.calculator(value,trade_type)
        return tax_price
    else:
        return value

@app.errorhandler(404)
def page_not_found(error):
    if request.is_xhr:
        return xtjson.json_params_error(message=u'错误404,你访问的页面未找到!')
    else:
        return render_template('common/common_404.html'),404

@app.errorhandler(401)
def auth_not_enough(error):
    if request.is_xhr:
        return xtjson.json_unpath_error(message=u'您访问该页面的权限不足!')
    else:
        return render_template('common/common_401.html'),401

if __name__ == '__main__':
    socketio.run(app,port=9000)
