#!/usr/bin/env  python3
# coding utf-8

import  socket


ip_port = ('127.0.0.1',8080)
tcp_socket_client  = socket.socket()
tcp_socket_client.connect(ip_port)

print('客户端启动')

while True:
    """
    """
    inp =  input('发送数据>>>>:').strip()
    tcp_socket_client.sendall(bytes(inp,'utf8'))

    if inp == 'exit':
        break

    server_response = tcp_socket_client.recv(1024)

    print('服务端响应数据>>>',str(server_response,'utf8'))

tcp_socket_client.close()