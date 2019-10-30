#!/usr/bin/env  python3
# coding utf-8

import  struct
import json



# res = struct.pack('i',1280)
# print(res,type(res),len(res))
#
#
# #  client.recv(4)
# obj = struct.unpack('i',res)
# print(obj[0])

#
# res = struct.pack('l',1280000000000000000)
# print(res,len(res))


headir_dic = {
    'filanem': 'a.txt',
    'md3': 'xxddxx',
    'total_size':22222222222222222222222222222222222222222222222222222222222222222222222222222222222,
}

header_json = json.dumps(headir_dic)
headir_bytes = header_json.encode('utf8')

obj = struct.pack('i',len(headir_bytes))
print(obj)


hadeir_dics = {
    'flane':'a.ext',
    'md5':'xdddse',
    'toal_size':123456789098765432123456789876543211234567898765434567898765432345678,
}
has = json.dumps(hadeir_dics)
has_bytes = has.encode('utf8')
obj1 = struct.pack('l',len(has_bytes))
print(obj1)