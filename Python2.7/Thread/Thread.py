#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Filename: thread

import time,threading

#新线程执行的代码
def loop():
    print 'thread %s is running...' %threading.current_thread().name
    n=0
    while n<5:
        n = n + 1
        print 'thread %s >>> %s' %(threading.current_thread().name,n)
        time.sleep(1)
    print 'thread %s ended.' %threading.current_thread().name
    print 'thread %s not ended.' %threading.current_thread().name
    print 'thread %s really ended.' %threading.current_thread().name

print 'thread %s id running...' %threading.current_thread().name
t = threading.Thread(target=loop)#,name='LoopThread'
t.start()
t.join()
print 'thread %s ended.' %threading.current_thread().name


#线程锁的概念

balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1=threading.Thread(target=run_thread,args=(5,))
t2=threading.Thread(target=run_thread,args=(8,))

t1.start()
t2.start()
t1.join()
t2.join()
print 'balance=',balance

