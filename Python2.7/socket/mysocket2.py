#!/user/bin/python
# -*- coding: utf-8 -*-

import socket

#create a scoket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#create a connection
s.connect(('127.0.0.1',8888))

#receive data
print s.recv(1024)
for data in ['Michael','Tracy','Sarah']:
    #send data
    s.send(data)
    print s.recv(1024)

#send exit command
s.send('exit')

#close connection
s.close()
