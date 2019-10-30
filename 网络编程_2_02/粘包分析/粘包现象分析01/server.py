#!/usr/bin/env  python3
# coding utf-8

import socket
# import subprocess
#


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  #
server.bind(('127.0.0.1',8080)) # 0 -65535  ;0 - 1024 给操作系统使用
server.listen(5)  # 最大挂起的连接数 5 个

print('starting....')

conn,addr = server.accept()
res1 =  conn.recv(1024)
print('第一次',res1)

res2 =  conn.recv(1024)
print('第二次',res2)

print('stop .....')
