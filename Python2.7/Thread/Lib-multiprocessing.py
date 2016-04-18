#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Filename:multiprocessing

from multiprocessing import Process,Pool,Queue
import os,time,random


#子进程要执行的代码
def run_proc(name):
    print 'Run child task %s (process:%s)...'%(name,os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()

if __name__=='__main__':
    print 'Parent process %s.'%os.getpid()
    p1 = Process(target=run_proc,args=('test',))
    print 'Process will start.'
    p1.start()
    p1.join()
    #Pool进程池的使用
    '''
    对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先
    调用close()，调用close()之后就不能继续添加新的Process了。
    '''
    print 'Process end.\n'
    p2=Pool(5) #默认是4
    print '******************************\nParent process %s.' % os.getpid()
    for i in range(5):
        p2.apply_async(run_proc,args=(i,))
    print 'Waiting for all subprocesses done...'
    p2.close()
    p2.join()
    print 'All subprocesses done.\n*********************************'

'''进程间的通信Queue，pipes等多种方式,以queue为例:
   在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据
'''
def write(q):
    for value in ['A','B','C']:
        print 'Put %s to queue...' %value
        q.put(value)
        time.sleep(random.random())

def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.'%value

if __name__=='__main__':
    #父进程创建Queue，并传给各个子进程
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()
    #等待pw结束
    pw.join()
    #pr进程是死循环，无法等待结束，只能强行终止
    pr.terminate()


