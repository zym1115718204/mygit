#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Filename:StringSort

import re

s = 'Python Django MySQL'

#一般切分字符串
l=s.split(' ')
new_s = str(l[2]+' '+l[1]+' '+l[0])
print new_s

#使用切片
new_s2 = str(s[14:19]+' '+s[7:13]+' '+s[0:6])
print new_s2

#使用正则表达式
l2 = re.split(r' ',s)
#print l2
new_s3 = str(l2[2]+' '+l2[1]+' '+l[0])
print new_s3

