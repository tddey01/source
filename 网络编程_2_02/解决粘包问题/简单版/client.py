#!/usr/bin/env  python3
# coding utf-8


import socket
import struct


phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 发起链接 到服务端
phone.connect(('127.0.0.1',8080))

#  发 收消息
while True:   # 通讯循环
    cmd = input('>>>').strip()  # cmd = ' '  空字符串
    if not cmd:continue
    phone.send(cmd.encode('utf8'))   # phone.send(b'')
    print('has send')

    # 先接收报头
    header = phone.recv(4)

    # total_size = 1024
    # 第二步 从 报头中解析出对真实数据的描述信息（数据的长度）
    total_size = struct.unpack('i', header)[0]

    # 第三步  接收真实的数据

    recv_size  = 0
    recv_data = b''
    while recv_size < total_size:
        res = phone.recv(1024)
        recv_data += res
        recv_size += 1024

    print('has recv')
    print(recv_data.decode('utf8'))

phone.close()