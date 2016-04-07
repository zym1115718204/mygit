#!/usr/bin/env python
# -*- coding:utf-8 -*-

from wsgiref.simple_server import make_server
from hello import application

#创建一个服务器，ip为空，端口为8000，处理函数是application
httpd = make_server('',9000,application)
print 'Server HTTP server on port 9000...'

#开始监听HTTP请求
httpd.serve_forever()