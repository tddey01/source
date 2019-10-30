#!/usr/bin/env  python3
# coding utf-8

from socket import *


server = socket(AF_INET,SOCK_DGRAM)     #
server.bind(('127.0.0.1',8080))

res1 = server.recvfrom(1024)
print(res1)
res2 = server.recvfrom(1024)
print(res2)


server.close()
