# coding:utf-8
from redis import StrictRedis
from functools import wraps
import json
redis=StrictRedis(host='127.0.0.1',port=9200,password='2312231223')


def to_dict(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        results=func(*args,**kwargs)
        result_dict=[json.loads(result) for result in results]
        return result_dict
    return wrapper

class RedisModel(object):
    def __init__(self,redis,model_name):
        self.__redis=redis
        self.model_name=model_name

    def add_model(self,model):
        model_json=model.to_json()
        return self.__redis.lpush(self.model_name,model_json)

    @to_dict
    def models(self,start=0,end=-1):
        return self.__redis.lrange(self.model_name,start,end)

    def set_model(self,model,value):
        for i in range(len(self.models)):
            if self.models[i]==model.to_dict():
                return self.__redis.lset(self.model_name,i,value)

    def delete_model(self):
        return self.__redis.rpop(self.model_name)

    def active_flush(self,model):
        self.add_model(model)
        count=len(self.models()) if self.models else 0
        if count>50:
            for i in range(count-50):
                self.delete_model()



class BBS_Redis(object):
    __redis=redis
    post=RedisModel(__redis,'second_post')
    comment=RedisModel(__redis,'second_comment')
    board=RedisModel(__redis,'second_board')

    @classmethod
    def get(cls,key):
        return cls.__redis.get(key)

    @classmethod
    def set(cls,key,value,ex=None):
        return cls.__redis.set(name=key,value=value,ex=ex)

    @classmethod
    def delete(cls,key):
        return cls.__redis.delete(key)

