# coding:utf-8
import cPickle


from redis import StrictRedis


from exts import db
# from constants import CACHE_NUM

redis=StrictRedis('192.168.1.4',port=6379,password='2312231223')

# table_mapping=dict(post='bbs_post',comment='bbs_comment')


class Redis_Model(object):

    def __init__(self,redis,table_name):
        self.__redis=redis
        self.table_name=table_name

    def to_str(self,model):
        return cPickle.dumps(model)

    def to_model(self,str):
        unbound_model=cPickle.loads(str)
        def bound_session(model):
            return db.session.merge(model)
        return bound_session(unbound_model)

    def add_model(self,model,rpush=False):
        str_model=self.to_str(model)
        if not rpush:
            return self.__redis.lpush(self.table_name,str_model)
        else:
            return self.__redis.rpush(self.table_name, str_model)

    def delete_model(self):
        return self.__redis.rpop(self.table_name)

    def get_model(self,start=0,end=-1):
        li=self.__redis.lrange(self.table_name,start,end)
        model_li=map(self.to_model,li)
        return model_li

    # def flush(self,model):
    #     self.add_model(model)
    #     num=len(self.get_model()) if self.get_model() else 0
    #     if num>CACHE_NUM:
    #         map(self.delete_model,list(range(num-CACHE_NUM)))


class Utils_Redis(object):
    __redis=redis

    post=Redis_Model(__redis,'customs_post')
    comment=Redis_Model(__redis,'customs_comment')

    @classmethod
    def get(cls,key):
        return cls.__redis.get(key)

    @classmethod
    def set(cls,key,value,ex=2*60):
        return cls.__redis.set(key,value,ex)

    @classmethod
    def delete(cls,key):
        return cls.__redis.delete(key)