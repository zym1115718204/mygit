#!/usr/bin/python
# -*- coding:utf-8 -*-
# Filename: DeleteRep

'''

'''
List=['123','abc','abc','123','cde','cde',1,2,2,3,4]

#错误去重算法1:，来源于作者zhangzheyuk（ChinaUnix），顺序对比法，但是对于相隔较远的重复项失效
def errorDelete1(s):
    StringList=s
    index = 1
    compare = 0
    length = len(StringList) - 1
    while index <= length:
        if cmp(StringList[index],StringList[compare]) == 0:
            del StringList[index]
            length -= 1                        #每次del之后List长度都减少
            if index == length + 1:         #限制最后出现末尾两个是重复的现象的终止
                break
        else:
             index += 1
             compare += 1
    print StringList

#去重方法：使用set去重,会导致顺序问题
def delete1(s):
    print list(set(s))

#去重方法：使用dict键值去重
def delete2(s):
    print {}.fromkeys(s).keys()

#去重方法：使用函数去重，顺序保持一致
def delete3(s):
    s0=[]
    [s0.append(x) for x in s if not x in s0]
    print s0

#去重方法：使用函数去重，顺序保持一致
def delete4(s):
    List0 = list(set(s))
    List0.sort(key=s.index)
    print List0

#这里测试出一个问题，同一个List在经过多次
def delete5(s5):
    s5.pop(2)
    s5.pop(2)
    s5.pop(3)
    s5.pop(5)
    print s5

#errorDelete1(List)
delete4(List)


