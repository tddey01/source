#!/usr/bin/env python
#_*_coding:utf-8_*_
"""
什么叫序列化？
序列化是指把内存里的数据类型转变成字符串，以使其能存储到硬盘或通过网络传输到远程，因为硬盘或网络传输时只能接受bytes

json，用于字符串 和 python数据类型间进行转换
Json模块提供了四个功能：dumps、dump、loads、load

只是把数据类型转成字符串存到内存里的意义
json.dumps json.loads
1 把你的内存数据 通过网络  共享给远程其他人
2 定义了不同语言的之前的交互规则
    1 纯文办 坏处 嵌套关系  不能共享处理复杂数据类型
    2 xml 坏处就是 占空间大
    3 json 简单  可读性好
    18:32  4354334          iphone    4000
    18:32  4354334          iphone    4000
"""

'''
data = {
    'roles':[
        {'role':'monstor','type':'pig','life':50},
        {'role':'hero',   'type':'关羽','life':80},
    ]
}

f = open(file='game_status',mode='w',encoding='utf8')

f.write(str(data))

f = open(file='game_status',mode='r',encoding='utf8')
d =  f.read()
d = eval(d)
print(d,['reles'])
'''
import json

# data = {
#     'roles':[
#         {'role':'monstor','type':'pig','life':50},
#         {'role':'hero',   'type':'关羽','life':80},
#     ]
# }
# d = json.dump(data)
# print(d,type(d))

# f = open(file='test.json',mode='w',encoding='utf8')
# # json.dump(data,f)
'''
d =  json.dumps(data)
d2 = json.loads(d)
print(d2,'reles')
'''

"""


f = open(file='test.json', mode='r', encoding='utf8')
data = json.load(f)
print(data['roles'])
"""
'''
f = open(file='json_file',mode='w',encoding='utf8')


d = {'name':'alex','age':22}

l = [1,2,3,4,'rain']

json.dump(d,f)
# json.dump(l,f)

'''

f = open(file='json_file',mode='r',encoding='utf8')
print(json.load(f))
