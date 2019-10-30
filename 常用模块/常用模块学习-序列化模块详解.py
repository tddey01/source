#!/usr/bin/env python
#_*_coding:utf-8_*_
"""
1 把内存数据，转成字符， 叫序列化
2 把字符转成内存数据类型 叫反序列化

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
