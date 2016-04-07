#!/usr/bin/python
# Filename: try_except.py

import sys

try:
    s = raw_input('Enter something --> ')
except EOFError:
    print '\nWhy did you do an EOF on me?'
    sys.exit() # exit the program
#第一个except用于缩小错误范围，如果是EOFError，将输出Why……
#将第一个except屏蔽之后，输出some……的错误提示，但是没法确定错误类型，故使用第一个缩小范围
except:
    print '\nSome error/exception occurred.'
    # here, we are not exiting the program

print 'Done'
