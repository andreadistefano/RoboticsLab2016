# -*- coding: utf-8 -*-

import socket
from time import sleep

HOST = 'localhost'      # The remote host
PORT = 25000            # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.sendall('Hello, world')
data = s.recv(1024)
print "Received:", data

newPort = int(data)
s.close()
sleep(0.25)

s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.connect((HOST, newPort))

for i in range(0, 100):
    s2.sendall(str(i))
    print i, s2.recv(1024)
    sleep(0.5)

s2.close()
