#!/usr/bin/env  python3
# coding utf-8

from socket import *


server = socket(AF_INET,SOCK_DGRAM)     #
server.bind(('127.0.0.1',8080))


while True:  # 通讯循环
    data,client_addr = server.recvfrom(1024)   # udp recvfrom
    print(data,client_addr)
    server.sendto(data.upper(),client_addr)

server.close()
