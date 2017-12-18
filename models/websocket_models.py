# coding:utf-8
from datetime import datetime

from flask import g


from exts import db
from models.base_models import BaseModel
from models.front_models import Front_User
from models.customs_models import Employee,Customs_User


class Message(db.Model):
    __tablename__='message'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    content=db.Column(db.String(200),nullable=False)
    create_time=db.Column(db.DateTime,default=datetime.now)

    front_user_id=db.Column(db.Integer,db.ForeignKey('front_user.id'))
    employee_id=db.Column(db.Integer,db.ForeignKey('employee.id'))
    customs_user_id=db.Column(db.Integer,db.ForeignKey('customs_user.id'))

    front_user_sender=db.relationship('Front_User',backref='sender_messages')
    employee_sender=db.relationship('Employee',backref='sender_messages')
    customs_user_sender=db.relationship('Customs_User',backref='sender_messages')

    front_user_receivers=db.relationship('Front_User',secondary='message_to_front_user',backref='receiver_messages')
    employee_receivers=db.relationship('Employee',secondary='message_to_employee',backref='receiver_messages')
    customs_user_receivers=db.relationship('Customs_User',secondary='message_to_customs_user',backref='receiver_messages')



    @property
    def sender(self):
        li=[self.front_user_sender,self.employee_sender,self.customs_user_sender]
        for i in li:
            if i is not None:
                return i

    @classmethod
    def str_handler(cls,value):
        model,id=value.split('__')

        return (model,id)


    @sender.setter
    def sender(self,value=None):
        assert value
        model,id=self.str_handler(value)
        try:
            send_model=eval(model).query.filter_by(id=id).first()
            send_name=model.lower()+'_sender'
            setattr(self,send_name,send_model)
        except Exception as e:
            print e



    def receivers(cls,value):
        assert value
        model, id = cls.str_handler(value)
        if id=='none':
            if model=='All':
                # 所有人喊话
                return list(Front_User.query)+list(Employee.query)+list(Customs_User)
            else:
                # 群聊
                return list(eval(model).query)

        else:

            # 单聊
            model=eval(model).query.filter_by(id=id).first()
            return model


    def set_receivers(self,value):
        model,id=self.str_handler(value)
        receiver_usernames = model.lower() + '_receivers'
        if id == 'none':
            if model == 'All':

                # front_users = Front_User.query.all()
                # customs_users = Customs_User.query.all()
                # employees = Employee.query.all()
                # self.front_user_receivers += front_users
                # self.customs_user_receivers += customs_users
                # self.employee_receivers += employees
                pass

            else:
                receiver_users=self.receivers(value)
                setattr(self, receiver_usernames, receiver_users)
        else:
            receiver_user = self.receivers(value)
            setattr(self, receiver_usernames, [receiver_user])




class Message_To_Front_User(db.Model):
    __tablename__='message_to_front_user'

    message_id=db.Column(db.Integer,db.ForeignKey('message.id'),primary_key=True)
    front_user_id=db.Column(db.Integer,db.ForeignKey('front_user.id'),primary_key=True)


class Message_To_Employee(db.Model):
    __tablename__ = 'message_to_employee'

    message_id = db.Column(db.Integer, db.ForeignKey('message.id'), primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), primary_key=True)

class Message_To_Customs_User(db.Model):
    __tablename__ = 'message_to_customs_user'

    message_id = db.Column(db.Integer, db.ForeignKey('message.id'), primary_key=True)
    customs_user_id = db.Column(db.Integer, db.ForeignKey('customs_user.id'), primary_key=True)







