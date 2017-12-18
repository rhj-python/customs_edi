# coding:utf-8
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
import json


from exts import db

class BaseModel(object):
    def to_dict(self):
        columns=self.__table__.columns
        dic={}
        for column in columns:
            value=getattr(self,column.name)
            if isinstance(value,datetime):
                value=value.strftime('%Y-%m-%d %H:%M:%S')
            dic[column.name]=value
        return dic

    def to_json(self):
        return json.dump(self.to_dict())



class BasePWDModel(BaseModel):
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_pwd):
        self._password = generate_password_hash(raw_pwd)

    def check_pwd(self, raw_pwd):
        return check_password_hash(self._password,raw_pwd) if raw_pwd else False
