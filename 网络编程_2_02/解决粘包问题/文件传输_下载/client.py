#!/usr/bin/env  python3
# coding utf-8


import socket
import struct
import json
import os

download_dir = r'/Users/tddey/project/source-py'

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 发起链接 到服务端
phone.connect(('127.0.0.1',8080))

#  发 收消息
while True:   # 通讯循环

    # 1 发送命令
    cmd = input('>>>').strip()  # get a.txt
    if not cmd:continue
    phone.send(cmd.encode('utf8'))
    print('has send')

    # 2 以写的方式 打开一个新文件，接收服务器发来过来的文件内容写入自己客户端的新文件
    obj = phone.recv(4)
    header_size= struct.unpack('i',obj)[0]

    #第二步 在接受报文
    header_bytes = phone.recv(header_size)
    # total_size = 1024

    # 第三步 从 报头中解析出对真实数据的描述信息（数据的长度）
    header_json = header_bytes.decode('utf8')
    header_dic = json.loads(header_json)

    print(header_dic)
    total_size = header_dic['total_size']

    filename = header_dic['filename']
    # 第四步  接收真实的数据
    with open('%s/%s' %(download_dir,filename),'wb') as f:

        recv_size  = 0
        while recv_size < total_size:
            line = phone.recv(1024)
            f.write(line)
            recv_size += len(line)
            print('总大小: %s 已下载 : %s ' % (total_size,recv_size))



phone.close()