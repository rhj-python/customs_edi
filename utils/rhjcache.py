# coding:utf-8
import memcache

mc=memcache.Client(['127.0.0.1:11211'],debug=True)

def get(key=None):
    if key:
        res=mc.get(key)
        return res
    return None

def set(key=None,value=None,time=2*60):
    if key and value:
        res=mc.set(key,value,time)
        return res
    return False

def delete(key=None):
    if key:
        res=mc.delete(key)
        return True
    return False
