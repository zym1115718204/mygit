#!/usr/bin/python
# Filename:lambda.py

#使用make_repeater函数在运行时创建新的函数对象，并且返回它
#lambda语句用来创建函数对象，本子上，lambda需要一个参数，后面紧跟单个表达式作为函数体
#表达式的值被这个新建的函数返回
#注意即使是print语句也不能用在lambda中，只能使用表达式
def make_repeater(n):
    return lambda s:s*n

twice=make_repeater(2)
ten=make_repeater(10)

print twice('word')
print twice(2)
print ten('hello!')
print ten(2)

#exec语句用来执行储存在字符串或者文件中的python语句
exec'print"Hello World!"'

#eval用来计算存储在字符串中的有效python表达式
#print eval('2*3')

mlt=eval('2*3')
print mlt

