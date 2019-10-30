#!/usr/bin/env  python3
# coding utf-8

from socket import  *

ip_port = ('127.0.0.1',8080)

tcp_socket_server = socket()
tcp_socket_server.bind(ip_port)
tcp_socket_server.listen(5)


while  1:
    conn,addr = tcp_socket_server.accept()
    print('客户端',addr)

    while 1:
        client_data = conn.recv(1024)
        print(client_data.decode('utf8'))

        if client_data.decode('utf8') == "exit":
            print('客户端断开连接，等待新的用户连接....')
            break

        print('连接数据...>>',str(client_data,'utf8'))

        response = input('响应数据>>>')
        conn.sendall(bytes(response,'utf8'))

    conn.close()
