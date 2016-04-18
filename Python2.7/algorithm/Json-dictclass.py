#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Filename: Json dict/class

import json

d=dict(name='Bob',age=20,score=88)
dr=json.dumps(d)
print dr
print json.loads(dr)

#class对象的json化
class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
class Teacher(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }
#def的函数只能适用于student
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

s = Student('Bob',20,88)
j_s = '{"age": 20, "score": 88, "name": "Bob"}'
t = Teacher('Lin',35)

#print json.dumps(s) #直接将对象进行Json转换会出错
print json.dumps(s,default=student2dict)
#反序列化的Student实例对象
print json.loads(j_s,object_hook=dict2student)
#<__main__.Student object at 0x000000000256B908>


#通用函数，将对象转换成dict
print json.dumps(s,default=lambda obj: obj.__dict__)
print json.dumps(t,default=lambda obj: obj.__dict__)
