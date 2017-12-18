# coding:utf-8

from flask import g

from models.front_models import Front_User
from models.customs_models import Customs_User,Employee
from models.websocket_models import Message
from exts import db

def handler_msg(value):
    model,id=value.split('__')
    model_name=model.lower()
    orm=model_name+'_receivers'
    return (model,id,model_name,orm)



def single_chat(sender, receivers):
    # ss_msgs=filter(lambda message:message.front_user_receivers==[front_model],g.employee.sender_messages)
    s_model, s_id,s_model_name,sr_orm= handler_msg(sender)
    r_model, r_id,r_model_name,rr_orm= handler_msg(receivers)

    # model 表的类名 id 记录的id model_name 表的类名小写
    # orm  message的这张表的接收人 例如 front_user_receivers


    sender_model = eval(s_model).query.filter_by(id=s_id).first()

    receiver_model = eval(r_model).query.filter_by(id=r_id).first()

    s_obj = sender_model.sender_messages
    r_obj = receiver_model.sender_messages


    ss_msgs = filter(lambda message: list(eval('message.%s' %(rr_orm))) == [receiver_model], s_obj)
    rs_msgs = filter(lambda message: list(eval('message.%s' %(sr_orm))) == [sender_model], r_obj)
    msgs=ss_msgs + rs_msgs
    msgs=sorted(msgs,key=lambda msg:msg.create_time)
    return msgs

def group_chat(receivers):
    r_model, r_id,r_model_name,rr_orm= handler_msg(receivers)
    msgs=Message.query.all()
    receiver_li=list(eval(r_model).query)
    messages=filter(lambda message:list(eval('message.%s' %(rr_orm)))==receiver_li,msgs)
    return messages

def all_chat():

    msg_li=list(Message.query)
    all_msgs=filter(lambda message:(message.front_user_receivers==[] and message.customs_user_receivers==[]
                    and message.employee_receivers==[]),msg_li)
    return all_msgs


class Online(object):
    online_set=set()

