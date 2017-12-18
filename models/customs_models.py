# coding:utf-8

from uuid import uuid4
from datetime import datetime

from werkzeug.security import generate_password_hash,check_password_hash


from exts import db
from base_models import BaseModel,BasePWDModel
from common_models import Company



class Customs_User(db.Model,BasePWDModel):
    __tablename__='customs_user'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),nullable=False)
    _password=db.Column(db.String(100),nullable=False)
    is_active=db.Column(db.Integer,default=1)

class Customs_Zone(db.Model,BaseModel):
    __tablename__='customs_zone'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(100),unique=True,nullable=False)

class Employee(db.Model,BasePWDModel):
    __tablename__='employee'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),nullable=False)
    _password=db.Column(db.String(100),nullable=False)
    create_time=db.Column(db.DateTime,default=datetime.now)
    is_active=db.Column(db.Integer,default=1)

    company_id=db.Column(db.ForeignKey('company.id'))

    company=db.relationship('Company',backref='employees')


class Triple_Status(db.Model,BaseModel):
    __tablename__='triple_status'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(100),nullable=False)

class Customs_Zone_Reply(db.Model,BaseModel):
    __tablename__='customs_zone_reply'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    content=db.Column(db.String(200),nullable=False)
    create_time=db.Column(db.DateTime,default=datetime.now)



class Triple_Agreement(db.Model,BaseModel):
    __tablename__='triple_agreement'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sign_name=db.Column(db.String(100))
    cancel_name=db.Column(db.String(100))

    sign_time=db.Column(db.DateTime)
    cancel_time=db.Column(db.DateTime)


    zone_id=db.Column(db.ForeignKey('customs_zone.id'))
    company_id=db.Column(db.ForeignKey('company.id'))
    status_id=db.Column(db.ForeignKey('triple_status.id'))
    reply_id=db.Column(db.ForeignKey('customs_zone_reply.id'))

    zone=db.relationship('Customs_Zone',backref='agreements')
    company=db.relationship('Company',backref='agreements')
    status=db.relationship('Triple_Status',backref='agreements')
    reply=db.relationship('Customs_Zone_Reply',backref='agreements')
