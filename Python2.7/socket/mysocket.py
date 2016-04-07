#!/user/bin/python
# -*- coding: utf-8 -*-

import socket

#create a scoket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#create a connection
s.connect(('www.sina.com.cn',80))

#create a request
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

#receive data
buffer=[]
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data=''.join(buffer)

#close connection
s.close

header,html=data.split('\r\n\r\n',1)
print header

with open('sina.html','wb') as f:
    f.write(html)
