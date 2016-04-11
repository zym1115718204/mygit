#!usr/bin/env python
# -*- coding:utf-8 -*-
__author__='Mr.ming'

#面对对象编程理解

class mapAndReduce():
    def __init__(self,s1,s2):
        self.s1=s1
        self.s2=s2

    def normalize(self,s):
        return map(lambda x:x[0].upper()+x[1:].lower(),s)

    def prod(self,s):
        #print reduce(lambda x,y:x*y,s)
        return reduce(lambda x,y:x*y,s)

    def start(self):
        print self.normalize(self.s1)
        print self.prod(self.s2)

    def start2(self,x,y):
        print self.normalize(x)
        print self.prod(y)

s1=['lisa','BOB','toM','Lucy']
s2=[1,2,3,4]
s3=[1,2,3,4,5,6]

mingming=mapAndReduce(s1,s2)
mingming.start()
mingming.start2(s1,s3)
