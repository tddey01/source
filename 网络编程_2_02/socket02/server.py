#!/usr/bin/env  python3
# coding utf-8
"""


"""
import socket

# 1 买手机

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# print(phone)

# 2 绑定手机卡

phone.bind(('127.0.0.1',8081)) # 0 -65535  ;0 - 1024 给操作系统使用

# 3 开机

phone.listen(5)  # 最大挂起的连接数 5 个

# 4 等电话
print('starting....')
# res = phone.accept()
conn,client_addr = phone.accept()
print(client_addr)
# 5 收发消息
while True:   # 通讯循环

    data = conn.recv(1024)  # 单位： bytes  2 1024代表最大接收1024个bytes
    print('客户端的数据',data)
    conn.send(data.upper())

# 挂电话
conn.close()
# 关机
phone.close()
print('stop .....')
