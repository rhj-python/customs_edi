# coding:utf-8
from datetime import datetime,timedelta,date
import json

from wtforms import (StringField,
IntegerField,BooleanField,DateTimeField,
DecimalField,DateField)
from wtforms.validators import (URL,
Length,EqualTo,InputRequired,Regexp,Email)
from flask import session,request,g
from werkzeug.datastructures import ImmutableMultiDict

from base_forms import BaseForm,DeclarationBaseForm
from common_forms import GraphCaptchaForm
from utils.rhjredis import Utils_Redis
from models.customs_models import (Customs_User,
Customs_Zone,Employee,Triple_Status,Triple_Agreement,
Customs_Zone_Reply,Company)
from models.common_models import (Import_Proxy_Agreement,
Export_Proxy_Agreement,Proxy,Pay_Mode,Transaction_Mode,
Trade_Mode,Agreement_Status,Tax_Mode,Use,Transport_Mode,
Currency,Tax_Free_Mode,Document,Document_Type,Import_Customs_Declaration,
Settlement_Mode,Export_Customs_Declaration)
from constants import CUSTOMS_SESSION_ID,EMPLOYEE_SESSION_ID,DELAY_CHECK_DAYS
from exts import db
from models.tax_rate_helper import Tax_Calculator
from models.manage_models import Role,Permission,Handler,Menu
from models.front_models import Front_User

class ManageResetPwdForm(BaseForm):
    old_password=StringField(validators=[InputRequired(message=u'请输入旧密码!'),Length(6,20,message=u'旧密码输入有误!')])
    new_password=StringField(validators=[InputRequired(message=u'请输入新密码!'),Length(6,20,message=u'密码长度在6-20字符之间!')])
    new_password_repeat=StringField(validators=[EqualTo('new_password',message=u'两次密码输入不一致!')])

    def validate(self):
        if not super(ManageResetPwdForm,self).validate():
            return False
        else:
            old_password=self.old_password.data
            new_password=self.new_password.data

            if not g.employee.check_pwd(old_password):
                self.old_password.errors.append(u'旧密码错误!')
                return False

            else:
                g.employee.password=new_password
                db.session.commit()
                return True

class ManageResetEmailForm(BaseForm):
    email=StringField(validators=[InputRequired(message=u'请输入邮箱!'),Email(message=u'邮箱格式有误!')])
    captcha=StringField(validators=[Length(6,6,message=u'验证码格式有误!'),InputRequired(message=u'请输入验证码!')])

    def validate(self):
        if not super(ManageResetEmailForm, self).validate():
            return False
        else:
            email=self.email.data

            captcha=self.captcha.data.lower()

            db_captcha=Utils_Redis.get(email)

            if not db_captcha or captcha!=db_captcha.lower():
                self.captcha.errors.append(u'邮件验证码输入有误!')
                return False
            else:
                g.employee.email=email
                db.session.commit()
                return True

class ManageAddEmployeeForm(BaseForm):
    username=StringField(validators=[Length(3,12,message=u'用户名长度在3-12字符之间!'),InputRequired(message=u'请输入用户名!')])
    email=StringField(validators=[Email(message=u'邮箱格式输入有误'),InputRequired(message=u'请输入邮箱!')])
    password=StringField(validators=[Length(6,20,message=u'密码长度在6-20位之间'),InputRequired(message=u'请输入密码!')])
    password_repeat=StringField(validators=[EqualTo('password')])

    def validate(self):

        if not super(ManageAddEmployeeForm, self).validate():
            return False
        else:
            username=self.username.data
            email=self.email.data
            password=self.password.data

            role_li=request.form.getlist('role_li[]')
            employee=Employee(username=username,password=password,email=email)
            company=Company.query.filter_by(id=1).first()
            employee.company=company

            db_employee=Employee.query.filter_by(email=email).first()

            if db_employee:
                self.email.errors.append(u'该员工已存在!请换个邮箱再进行添加!')
                return False

            if not role_li:
                self.username.errors.append(u'至少指定一个职位!')
                return False

            for role_id in role_li:
                role=Role.query.filter_by(id=role_id).first()
                employee.roles.append(role)

            db.session.commit()
            return True

class ManageEmployeeBaseForm(BaseForm):
    employee_id = StringField(validators=[InputRequired(message=u'必须指定员工ID!')])
    employee = ''
    def validate_employee_id(self,field):
        employee_id=field.data
        employee = Employee.query.filter_by(id=employee_id).first()
        if not employee:
            self.employee_id.errors.append(u'没有找到该员工!')
            return False
        else:
            self.employee=employee
            return True

class ManageEditEmployeeForm(ManageEmployeeBaseForm):
    def validate(self):
        if not super(ManageEditEmployeeForm, self).validate():
            return False
        else:
            role_li=request.form.getlist('role_li[]')

            if not role_li:
                self.employee_id.errors.append(u'请至少选择一项职位!')
                return False

            else:
                self.employee.roles=[]
                for role_id in role_li:
                    role=Role.query.filter_by(id=role_id).first()
                    self.employee.roles.append(role)
                db.session.commit()
                return True

class ManageBlackEmployeeForm(ManageEmployeeBaseForm):
    want_active=IntegerField(validators=[InputRequired(message=u'必须指定操作行为!')])


    def validate(self):
        if not super(ManageBlackEmployeeForm, self).validate():
            return False

        else:
            want_active=self.want_active.data
            if self.employee.is_active:
                if not want_active:
                    self.employee.is_active=0
                    db.session.commit()
                    return True
                else:
                    self.want_active.errors.append(u'该员工没有被拉黑，无需取消拉黑!')
                    return False

            else:
                if want_active:
                    self.employee.is_active=1
                    db.session.commit()
                    return True
                else:
                    self.want_active.errors.append(u'该员工已被拉黑，无需重复操作!')
                    return False


class ManageAddRoleForm(BaseForm):
    name=StringField(validators=[Length(2,50,message=u'职位名称长度不超过50字符'),InputRequired(message=u'请输入职位名称!')])
    desc=StringField()

    def validate(self):
        if not super(ManageAddRoleForm, self).validate():
            return False
        else:
            name=self.name.data
            desc=self.desc.data
            permission_li=request.form.getlist('permission_li[]')

            db_role=Role.query.filter_by(name=name).first()
            if db_role:
                self.name.errors.append(u'该职位已存在，请换个职位名称再试!')
                return False
            elif not permission_li:
                self.name.errors.append(u'请至少指定一项权限!')
                return False
            else:
                role=Role(name=name,desc=desc)
                for permission_id in permission_li:
                    permission=Permission.query.filter_by(id=permission_id).first()
                    if permission:
                        role.permissions.append(permission)
                db.session.commit()
                return True

class ManageRoleBaseForm(BaseForm):
    role_id=StringField(validators=[InputRequired(message=u'请指定职位ID')])

    role=''

    def validate_role_id(self,field):
        role_id=field.data
        role=Role.query.filter_by(id=role_id).first()

        if not role:
            self.role_id.errors.append(u'没有找到该职位!')
            return False
        else:
            self.role=role
            return True


class ManageEditRoleForm(ManageRoleBaseForm):
    def validate(self):
        if not super(ManageEditRoleForm, self).validate():
            return False
        else:
            permission_li=request.form.getlist('permission_li[]')
            self.role.permissions=[]
            for permission_id in permission_li:
                permission=Permission.query.filter_by(id=permission_id).first()
                self.role.permissions.append(permission)
            db.session.commit()
            return True


class ManageDeleteRoleForm(ManageRoleBaseForm):
    def validate(self):
        if not super(ManageDeleteRoleForm, self).validate():
            return False
        else:
            if list(self.role.permissions) or self.role.employees:
                self.role_id.errors.append(u'该职位下还有员工和对应的权限关系,不能移除')

                return False
            else:
                db.session.delete(self.role)
                db.session.commit()
                return True


class ManagePermissionBaseForm(BaseForm):
    name = StringField(validators=[InputRequired(message=u'请输入权限名称!')])
    desc = StringField(validators=[InputRequired(message=u'请输入权限描述!')])
    p_code = StringField(validators=[InputRequired(message=u'请输入权限代码!')])

    name_=''
    desc_=''
    p_code_=''

    handler_li=[]
    menu_li=[]

    def validate(self):
        if not super(ManagePermissionBaseForm, self).validate():
            return False
        else:
            name = self.name.data
            desc = self.desc.data
            p_code = self.p_code.data

            handler_li = request.form.get('handler_li[]')
            menu_li = request.form.get('menu_li[]')


            if not handler_li and not menu_li:
                self.name.errors.append(u'请至少选择一个权限')
                return False

            else:
                self.name_=name
                self.desc_=desc
                self.p_code_=p_code
                self.handler_li=handler_li
                self.menu_li=menu_li

                return True



class ManageAddPermissionForm(ManagePermissionBaseForm):

    def validate(self):
        if not super(ManageAddPermissionForm, self).validate():
            return False
        else:

            db_permission=Permission.query.filter_by(p_code=self.p_code_).first()
            if db_permission:
                self.p_code.errors.append(u'该权限已存在,请换个权限代码再试!')
                return False

            else:
                permission=Permission(name=self.name_,desc=self.desc_,p_code=self.p_code_)

                if self.handler_li:
                    for handler_id in self.handler_li:
                        handler=Handler.query.filter_by(id=handler_id).first()
                        if handler:
                            permission.handlers.append(handler)

                if self.menu_li:
                    for menu_id in self.menu_li:
                        menu =Menu.query.filter_by(id=menu_id).first()
                        if menu:
                            permission.menus.append(menu)

                db.session.add(permission)
                db.session.commit()
                return True

class ManageEditPermissionForm(ManagePermissionBaseForm):
    permission_id=IntegerField(validators=[InputRequired(message=u'请指定权限ID!')])

    def validate(self):
        if not super(ManageEditPermissionForm, self).validate():
            return False
        else:

            permission_id=self.permission_id.data
            permission=Permission.query.filter_by(id=permission_id).first()

            db_permission = Permission.query.filter_by(p_code=self.p_code_).first()



            if not permission:
                self.permission_id.errors.append(u'没有找到该权限!')
                return False
            elif db_permission and db_permission!=permission:
                self.p_code.errors.append(u'该权限已存在,请换个权限代码再试!')
                return False

            else:

                if self.handler_li:
                    for handler_id in self.handler_li:
                        handler = Handler.query.filter_by(id=handler_id).first()
                        if handler:
                            permission.handlers.append(handler)

                if self.menu_li:
                    for menu_id in self.menu_li:
                        menu = Menu.query.filter_by(id=menu_id).first()
                        if menu:
                            permission.menus.append(menu)
                permission.name=self.name_
                permission.desc=self.desc_
                permission.p_code=self.p_code_

                db.session.commit()
                return True

class ManageUserBlackForm(BaseForm):
    user_id=IntegerField(validators=[InputRequired(message=u'请输入用户ID!')])
    want_active=IntegerField(validators=[InputRequired(message=u'请制定操作行为!')])

    def validate(self):
        if not super(ManageUserBlackForm, self).validate():
            return False
        else:
            user_id=self.user_id.data
            want_active=self.want_active.data

            user=Front_User.query.filter_by(id=user_id).first()

            if not user:
                self.user_id.errors.append(u'没有找到该用户!')
                return False

            else:
                if user.is_active:
                    if not want_active:
                        user.is_active=0
                        db.session.commit()
                        return True
                    else:
                        self.want_active.errors.append(u'该用户没有被拉黑,无需取消拉黑!')
                        return False
                else:
                    if want_active:
                        user.is_active=1
                        db.session.commit()
                        return True
                    else:
                        self.want_active.errors.append(u'该用户已经被拉黑了，无需重复拉黑!')
                        return True










