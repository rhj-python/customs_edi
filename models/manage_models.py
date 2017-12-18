# coding:utf-8
from datetime import datetime



from exts import db
from models.base_models import BaseModel

class Role(db.Model,BaseModel):

    __tablename__='role'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(50),nullable=False)
    desc=db.Column(db.String(200))

    employees=db.relationship('Employee',secondary='employee_to_role',backref='roles')
    customs_users=db.relationship('Customs_User',secondary='customs_user_to_role',backref='roles')

class Employee_to_Role(db.Model,BaseModel):
    __tablename__='employee_to_role'

    employee_id=db.Column(db.Integer,db.ForeignKey('employee.id'),primary_key=True)
    role_id=db.Column(db.Integer,db.ForeignKey('role.id'),primary_key=True)

class Customs_User_To_Role(db.Model,BaseModel):

    __tablename__='customs_user_to_role'

    customs_user_id=db.Column(db.Integer,db.ForeignKey('customs_user.id'),primary_key=True)
    role_id=db.Column(db.Integer,db.ForeignKey('role.id'),primary_key=True)

class Permission(db.Model,BaseModel):
    __tablename__='permission'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(50),nullable=False)
    desc=db.Column(db.String(200))
    p_code=db.Column(db.String(100),nullable=False)

    roles=db.relationship('Role',secondary='role_to_permission',backref=db.backref('permissions',lazy='dynamic'))

class Role_To_Permission(db.Model,BaseModel):
    __tablename__='role_to_permission'

    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), primary_key=True)
    permission_id = db.Column(db.Integer, db.ForeignKey('permission.id'), primary_key=True)


class Handler(db.Model,BaseModel):
    __tablename__='handler'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.String(200))

    permissions=db.relationship('Permission',secondary='handler_to_permission',backref='handlers')


class Handler_To_Permission(db.Model,BaseModel):
    __tablename__='handler_to_permission'

    handler_id=db.Column(db.Integer,db.ForeignKey('handler.id'),primary_key=True)
    permission_id=db.Column(db.Integer,db.ForeignKey('permission.id'),primary_key=True)

class Menu(db.Model,BaseModel):
    __tablename__='menu'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.String(200))

    permissions=db.relationship('Permission',secondary='menu_to_permission',backref='menus')

class Menu_To_Permission(db.Model,BaseModel):
    __tablename__='menu_to_permission'

    menu_id=db.Column(db.Integer,db.ForeignKey('menu.id'),primary_key=True)
    permission_id=db.Column(db.Integer,db.ForeignKey('permission.id'),primary_key=True)

class File(db.Model,BaseModel):
    __tablename__='file'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    document_id=db.Column(db.Integer,db.ForeignKey('document.id'),unique=True)
    permission_id=db.Column(db.Integer,db.ForeignKey('permission.id'))

    document=db.relationship('Document',uselist=False,backref='file')
    permission=db.relationship('Permission',backref='files')







