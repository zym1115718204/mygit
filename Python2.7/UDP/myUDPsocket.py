#!/user/bin/python
# -*- coding: utf-8 -*-

import socket

#create a scoket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#send data
for data in ['Michael','Tray','Sarah']:
    #send data
    s.sendto(data,('127.0.0.1',8888))
    #receive
    print s.recv(1024)

#close
s.close()

