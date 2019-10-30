#!/usr/bin/env  python3
# coding utf-8

from  socket import  *

client = socket(AF_INET,SOCK_DGRAM)


while True:
    msg = input('>>>').strip()

    client.sendto(msg.encode('utf8'),('127.0.0.1',8080))     # udp 使用sendto
    data,server_addr = client.recvfrom(1024)
    print(data,server_addr)


client.close()