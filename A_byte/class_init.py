#!/usr/bin/python
# Filename: class_init.py

class Person:
    def __init__(self,name):
        self.name=name
    def sayHi(self):
        print 'Hello,my name is',self.name

#���ӣ���ԭcomment�������ݸ�Person()���Ӷ�ʵ������name
comment=raw_input('Enter a name:')

p=Person(comment)
p.sayHi()
