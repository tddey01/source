#!/usr/bin/env python
#_*_coding:utf-8_*_
"""
json 能序列化数据类型
 str,int,tuple,list,dict

pickle
    支持python 里的所有的数据类型
    缺点 只能在python里面使用
JSON:

优点：跨语言、体积小

缺点：只能支持int\str\list\tuple\dict

Pickle:

优点：专为python设计，支持python所有的数据类型

缺点：只能在python中使用，存储数据占空间大
"""
import pickle




# d = {'name':'alex','age':22}
# l = [1,2,3,4,'rain']

# pk = open(file='date.pkl',mode='wb')  #wb模式不建议指定字符编码
# print(pickle.dumps(d))  #装换成bayst类型
######################################
# # pickle.dump(d,pk)
# f = open(file='date.pkl',mode='rb')
# d = pickle.load(f)
# print(d)

def syahi():
    print('ddddd')

# print(pickle.dumps(syahi))


print()

