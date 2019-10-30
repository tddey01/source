#!/usr/bin/env  python3
# coding utf-8

from gevent import monkey,spawn;monkey.patch_all()
from  socket import *


def communicate(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:break
            conn.send(data.upper())
        except ConnectionAbortedError:
            break

    conn.close()


def server(ip,port):
    server = socket(AF_INET,SOCK_STREAM)
    server.bind(('127.0.0.1',8080))
    server.listen(5)

    while True:
        conn,addr = server.accept()
        spawn(communicate,conn)




    server.close()

if __name__ == '__main__':
    g = spawn(server,'127.0.0.1',8080)
    g.join()