# coding:utf-8
from datetime import datetime,timedelta

from flask import (
    Blueprint,render_template,request,url_for,redirect,g
)

from decorators.customs_decorators import customs_login_required
from utils import xtjson
from models.front_models import Front_User
from models.customs_models import Customs_User,Employee
from models.websocket_models import Message

bp=Blueprint('chart',__name__,url_prefix='/chart')

@bp.route('/',methods=['GET'])
@customs_login_required
def chart_index():
    return render_template('chart/chart_index.html')

@bp.route('/trade_num_chart/',methods=['GET'])
def chart_trade_num_chart():
    data=[
        dict(name=u'出口', data=[840, 645, 700, 850, 825, 770, 586, 667, 754, 877, 935, 1053]),
        dict(name=u'进口',data=[453,280,427,557,603,524,481,587,820,620,750,819]),
    ]
    return xtjson.json_result(data=data)

@bp.route('/user_chart/',methods=['get'])
def chart_user_chart():
    employees=Employee.query.count()
    customs_users=Customs_User.query.count()
    front_users=Front_User.query.count()
    total_users=employees+customs_users+front_users
    data=[[u'员工',employees*100//total_users],
          [u'海关',customs_users*100//total_users],
          [u'客户',front_users*100//total_users],
          ]

    return xtjson.json_result(data=data)

@bp.route('/trade_contrast_chart/',methods=['GET'])
def chart_trade_contrast_chart():
    data=[
        dict(name='2015年报关情况',data=[12472,6545,19017]),
        dict(name='2016年报关情况',data=[9502,6921,16423])
    ]

    return xtjson.json_result(data=data)

@bp.route('/budget_spend_chart/',methods=['GET'])
def chart_budget_spend_chart():
    data=[
        dict(name=u'预算',data=[210000,160000,110000,150000,170000,200000],pointPalcement='on'),
        dict(name=u'支出',data=[250000,80000,60000,130000,300000,160000],pointPalcement='on'),
    ]
    return xtjson.json_result(data=data)


@bp.route('/message_info_chart/',methods=['GET'])
def chart_message_info_chart():
    li=[]
    li_2=[]
    for i in xrange(7):
        pre_day=datetime.now()-timedelta(days=i+1)
        next_day=datetime.now()-timedelta(days=i)
        messages=Message.query.filter(Message.create_time.between(pre_day,next_day)).count()
        li.append(messages)
        li_2.append(next_day.strftime('%m-%d'))
    li.sort()
    li_2.sort()
    print li
    data=[dict(name=u'用户聊天记录数',data=li)]

    return xtjson.json_result(data=data,kwargs=dict(li=li_2))