#!/usr/bin/env  python3
# coding utf-8
from  socket import *

client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8080))


while True:
    msg = input('>>>: ').strip()
    if not  msg :continue
    client.send(msg.encode('utf8'))
    data = client.recv(1024)
    print(data.decode('utf8'))

client.close()