#!/usr/bin/env  python3
# coding utf-8


import socket


phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  #
phone.bind(('127.0.0.1',8080)) # 0 -65535  ;0 - 1024 给操作系统使用
phone.listen(5)  # 最大挂起的连接数 5 个



print('starting....')
conn,client_addr = phone.accept()
print(client_addr)


#  收发消息
while True:   # 通讯循环
    try :

        data = conn.recv(1024)  # 单位： bytes  2 1024代表最大接收1024个bytes
        if not data:break  # 适用于linux操作系统
        print('客户端的数据',data)
        conn.send(data.upper())
    except ConnectionAbortedError as e:  # 适用于windows机器
        print('ConnectionAbortedError',e)
        break
# 挂电话
conn.close()
# 关机
phone.close()
print('stop .....')
