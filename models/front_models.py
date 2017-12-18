# coding:utf-8
from uuid import uuid4
from datetime import datetime



from exts import db
from models.base_models import BaseModel,BasePWDModel
from common_models import Company

class Front_User(db.Model,BasePWDModel):
    __tablename__='front_user'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    uuid=db.Column(db.String(100),unique=True,default=lambda:str(uuid4()))
    username=db.Column(db.String(20),nullable=False)
    _password=db.Column(db.String(100),nullable=False)
    phone=db.Column(db.String(11),nullable=False,unique=True)
    create_time=db.Column(db.DateTime,default=datetime.now)
    is_active=db.Column(db.Integer,default=1)

    company_id=db.Column(db.Integer,db.ForeignKey('company.id'))

    company=db.relationship('Company',backref='users')

