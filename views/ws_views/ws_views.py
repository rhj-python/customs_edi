# coding:utf-8
from datetime import datetime

from flask import (Blueprint,
render_template,url_for,g,redirect,request)

from exts import db,socketio,app
from flask_socketio import emit,join_room,leave_room
from models.websocket_models import Message
from models.customs_models import Customs_User,Employee
from models.front_models import Front_User
from decorators.customs_decorators import customs_login_required
from models.ws_model_helper import single_chat,group_chat,all_chat
from models.ws_model_helper import Online
from utils import xtjson

bp=Blueprint('ws',__name__,url_prefix='/ws')


@bp.route('/ws_msg_single/',methods=['GET'])
@customs_login_required
def ws_msg_single():
    front_users=Front_User.query.all()
    employees=Employee.query.all()
    customs_users=Customs_User.query.all()
    online_set=Online.online_set
    context=dict(front_users=front_users,employees=employees,
                 customs_users=customs_users,online_set=online_set)
    return render_template('ws/ws_msg_single.html',**context)

@bp.route('/ws_msg_single_flush/',methods=['GET'])
@customs_login_required
def ws_msg_single_flush():
    front_users = Front_User.query.all()
    employees = Employee.query.all()
    customs_users = Customs_User.query.all()
    online_set = Online.online_set
    context = dict(front_users=front_users, employees=employees,
                   customs_users=customs_users, online_set=online_set)
    html=render_template('ws/ws_msg_single_flush.html', **context)
    return xtjson.json_result(data=html)


@bp.route('/ws_msg_single_detail/<string:model_name>/<string:receiver_name>/')
@customs_login_required
def ws_msg_single_detail(model_name,receiver_name):
    model=eval(model_name).query.filter_by(username=receiver_name).first()
    if g.employee:
        s_model=g.employee.__class__.__name__
        s_id=g.employee.id
    else:
        s_model=g.customs_user.__class__.__name__
        s_id = g.customs_user.id
    sender='%s__%s' %(s_model,s_id)
    receiver='%s__%s' %(model_name,model.id)
    messages=single_chat(sender,receiver)

    context=dict(model=model,model_name=model_name,messages=messages)
    return render_template('ws/ws_msg_single_detail.html',**context)



@bp.route('/ws_msg_group/',methods=['GET'])
@customs_login_required
def ws_msg_group():
    groups=[Employee,Customs_User,Front_User]
    context=dict(groups=groups)
    return render_template('ws/ws_msg_group.html',**context)

@bp.route('/ws_msg_group_detail/<string:group_name>/',methods=['GET'])
@customs_login_required
def ws_msg_group_detail(group_name):
    receiver='%s__%s' %(group_name,'none')
    messages=group_chat(receiver)

    context=dict(group_name=group_name,messages=messages)
    return render_template('ws/ws_msg_group_detail.html',**context)

@bp.route('/ws_msg_all/',methods=['GET'])
@customs_login_required
def ws_msg_all():
    messages=all_chat()
    context=dict(messages=messages)

    return render_template('ws/ws_msg_all.html',**context)

@socketio.on('my_event')
def ws_my_event(data):
    content=data.get('content')
    create_time=datetime.now()
    sender=data.get('sender')
    receiver = data.get('receiver')
    # sender_name = data.get('sender_name')

    if not 'none' in receiver:
        join_room(receiver)

    data.update(create_time=create_time)

    context=dict(message=data,self_user=None)

    html_left=render_template('ws/ws_msg_tpl_left.html', **context)
    html_right=render_template('ws/ws_msg_tpl_right.html', **context)

    data=dict(html_left=html_left,html_right=html_right,sender=sender)

    socketio.emit('my_event',data,room=receiver)


    message=Message(content=content,create_time=create_time)
    message.sender=sender
    message.set_receivers(receiver)

    if not 'none' in receiver:
        leave_room(receiver)
    db.session.add(message)
    db.session.commit()


# @socketio.on('my_event')
# def ws_my_message(data):
#     sender=data.get('sender')
#     receiver=data.get('receiver')
#     data={'sender':sender,'receiver':receiver}
#     emit('my_message',data)


@socketio.on('my_broadcast')
def ws_my_broadcast(data):
    content = data.get('content')
    create_time = datetime.now()
    sender = data.get('sender')
    receiver = data.get('receiver')
    # sender_name = data.get('sender_name')


    data.update(create_time=create_time)

    context = dict(message=data, self_user=None)

    html_left = render_template('ws/ws_msg_tpl_left.html', **context)
    html_right = render_template('ws/ws_msg_tpl_right.html', **context)

    data = dict(html_left=html_left, html_right=html_right, sender=sender)

    print '-' * 30
    print receiver
    print '-' * 30


    socketio.emit('my_broadcast', data, broadcast=True)

    message = Message(content=content, create_time=create_time)
    message.sender = sender
    message.set_receivers(receiver)

    db.session.add(message)
    db.session.commit()


@socketio.on('join_connect')
def ws_join_connect(data):
    self_room=data.get('self_room')
    self_group=data.get('self_group')

    join_room(self_room)
    if self_group:
        for s in self_group:
            join_room(s)

@socketio.on('join')
def ws_join(data):
    receiver=data.get('receiver')
    join_room(receiver)


@socketio.on('leave')
def ws_leave(data):
    receiver = data.get('receiver')
    leave_room(receiver)

@socketio.on('conn')
def ws_conn(data):
    sender=data.get('sender')
    Online.online_set.add(sender)

@socketio.on('dis_conn')
def ws_dis_conn(data):
    sender=data.get('sender')
    Online.online_set.remove(sender)