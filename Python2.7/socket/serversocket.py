#!/user/bin/python
# -*- coding: utf-8 -*-

import socket
import time,threading

#deal with new thread
def tcplink(sock,addr):
    print 'Accept new connection from %s:%s...'%addr
    sock.send('Welcome!')
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if data=='exit' or not data:
            break
        sock.send('Hello, %s!'%data)
    sock.close()
    print 'Connection from %s:%s closed.'%addr

#create a scoket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind point
s.bind(('127.0.0.1',8888))
s.listen(5)
print 'Waiting for connection...'

#create a thread
while True:
    #recive a connection
    sock,addr = s.accept()
    #create a thread
    t = threading.Thread(target=tcplink,args=(sock,addr))
    t.start()

