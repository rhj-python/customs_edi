# coding:utf-8
from functools import wraps

from flask import (session,
redirect,url_for,request,g,abort)

from models.customs_models import Customs_User,Employee
from constants import CUSTOMS_SESSION_ID,EMPLOYEE_SESSION_ID
from permissions.customs_permissions import Permission_Handler

def customs_login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        customs_id=session.get(CUSTOMS_SESSION_ID)
        employee_id=session.get(EMPLOYEE_SESSION_ID)
        if customs_id:
            customs_user=Customs_User.query.filter_by(id=customs_id).first()
            if customs_user:
                return func(*args,**kwargs)
            else:
                return redirect(url_for('customs_account.customs_choice_login',next=request.path))
        elif employee_id:
            employee = Employee.query.filter_by(id=employee_id).first()
            if employee:
                return func(*args, **kwargs)
            else:
                return redirect(url_for('customs_account.customs_choice_login', next=request.path))

        else:
            return redirect(url_for('customs_account.customs_choice_login',next=request.path))
    return wrapper


def permission_required(type,p_code):
    def outer(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print '-'*30
            print g.employee
            print '-'*30
            has_permission=Permission_Handler.has_permission(g.employee,type,p_code)
            return func(*args,**kwargs) if has_permission else abort(401)
        return wrapper
    return outer


def manage_permission_required(func):
    return permission_required('handler','manage_view')(func)

def customs_permission_required(func):
    return permission_required('handler','customs_view')(func)

def customs_check_permission_required(func):
    return permission_required('handler','customs_check_view')(func)
