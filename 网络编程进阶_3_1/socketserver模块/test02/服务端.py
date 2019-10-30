#!/usr/bin/env  python3
# coding utf-8

import  socketserver
"""
socketserver  使用模式
1  自定义功能类  
  class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
    pass 


2  
server1 = socketserver.ThreadingTCPServer(('127.0.0.1',8080),MyServer)


3
server1.serve_forever()


"""

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        """
        并发业务逻辑
        conn
        :return:
        """

        while 1:
            client_data = self.request.recv(1024)
            print(client_data.decode('utf8'))

            if client_data.decode('utf8') == "exit":
                print('客户端断开连接，等待新的用户连接....')
                break

            print('连接数据...>>', str(client_data, 'utf8'))

            response = input('响应数据>>>')
            self.request.sendall(bytes(response, 'utf8'))

        self.request.close()
# 1 self.socket  2 self.socket.bind() 3 self.socket.listen(5)
server1 = socketserver.ThreadingTCPServer(('127.0.0.1',8080),MyServer)


server1.serve_forever()






