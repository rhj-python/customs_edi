# coding:utf-8
from flask import g

from models.manage_models import (Handler
,Menu,File,Permission,Role)
from models.customs_models import Employee,Customs_User


class Permission_Handler(object):
    permission_model=dict(handler=Handler,menu=Menu,file=File)

    @classmethod
    def _get_user_permissions(cls,user):
        permissions=[]
        roles=user.roles if user else []
        for role in roles:
            permissions+=role.permissions
        return set(permissions)

    @classmethod
    def _get_obj_permissions(cls,type,obj_name):
        model=cls.permission_model.get(type)
        if not model or not obj_name:
            return None
        else:
            obj=model.query.filter_by(name=obj_name).first()
            if obj:
                return obj.permissions
            else:
                return []

    @classmethod
    def has_permission(cls,user,type,obj_name):
        obj_permissions=cls._get_obj_permissions(type,obj_name)
        user_p=cls.user_permissions(user)
        for permission in obj_permissions:
            if permission not in user_p:
                return False
        return True

    @classmethod
    def user_permissions(cls,user):
        return cls._get_user_permissions(user)
