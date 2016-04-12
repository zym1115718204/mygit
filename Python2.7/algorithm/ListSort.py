#!/usr/bin/python
# -*- coding:utf-8 -*-
# Filename: ListSort

List=[1,9,7,8,6,4,5,3,2]
List1=[1,2,4,3,1]

def bubble_sort(s):
    if len(s)==0:
        return None
    list = s
    for i in range(len(list)):
        for j in range(i,len(list)):
            if list[i]>list[j]:
                temp =list[j]
                list[j]=list[i]
                list[i]=temp
    #print list

def selection_sort(s):
    if len(s)==0:
        return None
    list = s
    for i in range(len(list)):
        postion = i
        for j in range(i,len(list)):
            if list[postion]>list[j]:
                postion = j
            if postion != i:
                temp = list[j]
                list[j] = list[i]
                list[i] = temp
    #print list

def insertion_sort(s):
    if len(s)==0:
        return None
    list = s
    if len(list)>0:
        for i in range(len(list)):
            while i>1 and list[i] < list[i-1]:
                temp = list[i-1]
                list[i-1] = list[i]
                list[i] = temp
                i = i-1
            #print list
    #print list

if __name__=='__main__':
    from timeit import Timer
    t1=Timer("bubble_sort(range(1000,0,-1))","from __main__ import bubble_sort")
    t2=Timer("selection_sort(range(1000,0,-1))","from __main__ import selection_sort")
    t3=Timer("insertion_sort(range(1000,0,-1))","from __main__ import insertion_sort")
    #print t1.timeit(100)
    #print t2.timeit(100)
    #print t3.timeit(100)
    print t1.repeat(3,10)
    print t2.repeat(3,10)
    print t3.repeat(3,10)

#bubble_sort(List)
#selection_sort(List)
#insertion_sort(List)
