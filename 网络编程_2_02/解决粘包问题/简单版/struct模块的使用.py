#!/usr/bin/env  python3
# coding utf-8

import  struct

res = struct.pack('i',1280)
# print(res,type(res),len(res))
#
#
# #  client.recv(4)
# obj = struct.unpack('i',res)
# print(obj[0])


res = struct.pack('l',1280000000000000000)
print(res,len(res))