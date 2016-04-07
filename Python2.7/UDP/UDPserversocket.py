#!/user/bin/python
# -*- coding: utf-8 -*-

import socket

#create a scoket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# bind point
s.bind(('127.0.0.1',8888))

print 'Bind UDP on 8888'
while True:
    #receive data
    data,addr=s.recvfrom(1024)
    print 'Receive data from %s:%s...'%addr
    #send data
    s.sendto('Hello,%s!'%data,addr)


#close
s.close()