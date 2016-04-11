#!usr/bin/env python
# -*- coding:utf-8 -*-

#装饰器decorator

#定义无参数的decorator
def log1(func):
    def wrapper(*args,**kw):
        print 'call %s()' %func.__name__
        return func(*args,**kw)
    return wrapper

#定义有参数的decorator
def log2(text=''):
    def decorator(func):
        def wrapper(*args,**kw):
            print '%s call %s()' %(text,func.__name__)
            return func(*args,**kw)
        return wrapper
    return decorator

#定义有参数的decorator,前后打印
def log3(text=''):
    def decorator(func):
        def wrapper(*args,**kw):
            print 'Begin print......'                 #调用前打印
            if text == '':
                print 'Call %s()' %func.__name__
            else:
                print '%s,call %s()' %(text,func.__name__)
            result = func(*args,**kw)
            print 'End print......'                   #调用后打印
            return result
        return wrapper
    return decorator

@log3('Hello')
def now():
    print '2016.4.11'

now()
