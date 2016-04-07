#!/usr/bin/python
# Filename: class_init.py

class Person:
    def __init__(self,name):
        self.name=name
    def sayHi(self):
        print 'Hello,my name is',self.name

#附加：将原comment参数传递给Person()，从而实现输入name
comment=raw_input('Enter a name:')

p=Person(comment)
p.sayHi()
