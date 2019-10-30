#!/usr/bin/env  python3
# coding utf-8
"""
shell 测试
"""

import socket
import subprocess
import struct
import  json


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
            headir_dic = {
                'filanem':'a.txt',
                'md3':'xxddxx',
                'total_size': len(stdout)+len(stderr)
            }

            header_json = json.dumps(headir_dic)
            header_bytes = header_json.encode('utf8')
            #  第二步  先发送报头长度
            conn.send(struct.pack('i', len(header_bytes)))

            # 第三步 在发送报头
            conn.send(header_bytes)


           # 第四步  在发送真实数据
            conn.send(stdout)
            conn.send(stderr)

        except ConnectionAbortedError as e:  # 适用于windows机器
            print('ConnectionAbortedError',e)
            break
    # 挂电话
    conn.close()
# 关机
phone.close()
print('stop .....')

