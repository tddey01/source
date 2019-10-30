#!/usr/bin/env  python3
# coding utf-8


from socket import *
from multiprocessing import Process

import time,os

def talk(conn):
    while True:
        try :
            data = conn.recv(1024)
            if not data:break
            conn.send(data.upper())
        except ConnectionAbortedError:
            break

def server(ip,port):
    """

    :param ip:
    :param port:
    :return:
    """
    server = socket(AF_INET,SOCK_STREAM)
    server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    server.bind((ip,port))
    server.listen(5)

    while True:
        conn,add = server.accept()
        p = Process(target=talk,args=(conn,))
        p.start()

    server.close()

if __name__ == '__main__':
    server('127.0.0.1',8080)