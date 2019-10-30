#!/usr/bin/env  python3
# coding utf-8


import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 发起链接 到服务端
phone.connect(('127.0.0.1',8080))

#  发 收消息
while True:   # 通讯循环
    cmd = input('>>>').strip()  # cmd = ' '  空字符串
    if not cmd:continue
    phone.send(cmd.encode('utf8'))   # phone.send(b'')
    print('has send')
    data = phone.recv(1024)  # 1024是一个坑
    print('has recv')
    print(data.decode('utf8'))

phone.close()