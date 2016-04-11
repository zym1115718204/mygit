#!usr/bin/env python
# -*-coding:utf-8-*-

#装饰器decorator

#定义无参数的decorator
def log1(func):
    def wrapper(*args,**kw):
        print 'call %s()' %func.__name__
        return func(*args,**kw)
    return wrapper

#定义有参数的decorator
def log2(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print '%s,call %s()' %(text,func.__name__)
            return func(*args,**kw)
        return wrapper
    return decorator

@log2('Hello')
def now():
    print '2016.4.11'

now()
