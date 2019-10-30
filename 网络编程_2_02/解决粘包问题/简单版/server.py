#!/usr/bin/env  python3
# coding utf-8
"""
shell 测试
"""

import socket
import subprocess
import struct


phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  #
phone.bind(('127.0.0.1',8080)) # 0 -65535  ;0 - 1024 给操作系统使用
phone.listen(5)  # 最大挂起的连接数 5 个



print('starting....')
while True:   # 链接循序
    conn,client_addr = phone.accept()
    print(client_addr)
    #  收发消息
    while True:   # 通讯循环
        try :
           # 接收 下发指令
            cmd = conn.recv(8096)  # 单位： bytes  2 1024代表最大接收1024个bytes
            if not cmd:break  # 适用于linux操作系统
            obj = subprocess.Popen(cmd.decode('utf8'),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            stdout  = obj.stdout.read()
            stderr  = obj.stderr.read()

            print('客户端的数据',cmd)
           # 执行下发指令  德到指令返回结果

           # 指令结果返回给发起客户端
           # 第一步 制作固定长度的报头
            total_size = len(stdout) + len(stderr)
            header = struct.pack('i',total_size)

            # 第二步 把报头长度发给客户端
            # total_size = (len(stdout)+ len(stderr))
            # conn.send(str(total_size).encode('utf8'))
            conn.send(header)
           # 第三步 在发送真实的数据

            conn.send(stdout)
            conn.send(stderr)

            # conn.send(stdout+stderr)  # + 可以优化的点

        except ConnectionAbortedError as e:  # 适用于windows机器
            print('ConnectionAbortedError',e)
            break
    # 挂电话
    conn.close()
# 关机
phone.close()
print('stop .....')
