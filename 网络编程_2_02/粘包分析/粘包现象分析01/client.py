#!/usr/bin/env  python3
# coding utf-8


import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 发起链接 到服务端
client.connect(('127.0.0.1',8080))

client.send('hello'.encode('utf8'))
client.send('word'.encode('utf8'))
