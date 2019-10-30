#!/usr/bin/env  python3
# coding utf-8
"""
shell 测试
"""

import socket
import subprocess
import struct
import  json
import os

share_dir = r'/Users/tddey/project/source-py'

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
           #  1 接收 下发指令
            res  = conn.recv(8096)  #  b 'get  a.txt
            if not res:break  # 适用于linux操作系统

            # 2 解析命令  提取相关命令参数
            cmds = res.decode('utf8').split() # ['get','a.txt]
            filename = cmds[1]

            # 3 已读的方式打开文件，读取文件内容 发送给客户端

           # 执行下发指令  德到指令返回结果

           # 指令结果返回给发起客户端
           # 第一步 制作固定长度的报头
            headir_dic = {
                'filanem':filename,
                'md3':'xxddxx',
                'total_size':os.path.getsize(r'%s/%s' %(share_dir,filename))
            }

            header_json = json.dumps(headir_dic)
            header_bytes = header_json.encode('utf8')
            #  第二步  先发送报头长度
            conn.send(struct.pack('i', len(header_bytes)))

            # 第三步 在发送报头
            conn.send(header_bytes)


           # 第四步  在发送真实数据
            with open('%s/%s' %(share_dir,filename),'rb') as f:

                 for line in f:
                     conn.send(line)

        except ConnectionAbortedError as e:  # 适用于windows机器
            print('ConnectionAbortedError',e)
            break
    # 挂电话
    conn.close()
# 关机
phone.close()
print('stop .....')

