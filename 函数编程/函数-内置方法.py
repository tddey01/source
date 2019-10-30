#!/usr/bin/env python
# -*- coding: utf-8 -*-
# abs() 取绝对值
# dict()  把一个数据转成一个字典
# min() 取出最小的值
# max() 取出最大的值
# all()
# bool() 判断一个值是不是True
# dir()  输出当前程序的所有变量
# any([False,0])  人一个值是True 就返回True
# hex(12)  转成16进制
# divmod(10,3)    整除取余
"""
# >>> a = (1,2,5,7,-1,-7)
# >>> min(a)
# -7
# >>> max(a)
# 7
#
# >>> bool(a)
# True
# >>> a.append(0)
# >>> all(a)
# False
# >>> any([False,0])  人一个值是True 就返回True
# False
# >>> any([False,0,1])
# True
# >>> dir()  输出当前程序的所有变量
# ['__builtins__', 'a', 'sys']
# >>> c = 3
# >>> dir()
# ['__builtins__', 'a', 'c', 'sys']
# >>> hex(12)  转成16进制
# '0xc'
# >>> s = slice(1,2,4)
# >>> s
# slice(1, 2, 4)   切片
# >>> l = list(range(10))
# >>> l
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> l[s]
# [1]
# >>> s
# slice(1, 2, 4)
# >>> l[1:3]
# [1, 2]
# >>> l[s]
# [1]
# >>> s = slice(1,2,7)
# >>> l[s]
# [1]
# >>> l
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> divmod(10,3)    整除取余
# (3, 1)
# >>> l=range(10)
# >>> l=list(range(10))
# >>> l
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> sorted(l)   排序
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> sorted(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 18, 138]
# >>> d = {}
# >>> for i in range(20):
# ...     d[i] = i -50
# ...
# >>> d
# {0: -50, 1: -49, 2: -48, 3: -47, 4: -46, 5: -45, 6: -44, 7: -43, 8: -42, 9: -41, 10: -40, 11: -39, 12: -38, 13: -37, 14: -36, 15: -35, 16: -34, 17: -33, 18: -32, 19: -31}
# >>> d.items()
# dict_items([(0, -50), (1, -49), (2, -48), (3, -47), (4, -46), (5, -45), (6, -44), (7, -43), (8, -42), (9, -41), (10, -40), (11, -39), (12, -38), (13, -37), (14, -36), (15, -35), (16, -34), (17, -33), (18, -32), (19, -31)])
# >>> sorted(d.items()) 从小到大
# [(0, -50), (1, -49), (2, -48), (3, -47), (4, -46), (5, -45), (6, -44), (7, -43), (8, -42), (9, -41), (10, -40), (11, -39), (12, -38), (13, -37), (14, -36), (15, -35), (16, -34), (17, -33), (18, -32), (19, -31)]
# >>> sorted(d.items(),key=lambda  x:x[1],reverse=True)  从大到小
# [(0, 399), (19, -31), (18, -32), (17, -33), (16, -34), (15, -35), (14, -36), (13, -37), (12, -38), (11, -39), (10, -40), (9, -41), (8, -42), (7, -43), (6, -44), (5, -45), (4, -46), (3, -47), (2, -48), (1, -49)]
# >>> oct(10) 十进制转成8进制
# '0o12'
# >>> bin(10) 十进制转成2进制
# '0b1010'
# >>> f = "1+3/2"
# >>> f
# '1+3/2'
# >>> eval(f)   把字符串转成代码 可执行  只能处理单行代码
# 2.5

# >>> code  = '''
# ... if 3 > 5:
# ...     print('3 logger then 5')
# ... else:
# ...     print('sss')
# ... '''
# >>> exec(code)   exec可以执行多行代码
# sss

# code  = '''
# def  foo():
#     print('run foo')
#     return  1234
# foo()
# '''
# res = eval('1+2+3')
# re2 = exec('1+2+3')
# # exec(code)
# # res = exec(code)
# # print(res)
# print(res,re2)
# >>> ord('a')      ascii码 位置
# 97
import operator
# >>> a = [1,4,6,-1,3,0]
# >>> a
# [1, 4, 6, -1, 3, 0]
# >>> sum(a)      求和
# 13

# >>> s.encode('utf-8')  适用于大字符串或者列表修改元数据在内存
# >>> s = bytearray(s)            转成byte类型 才能被修改
# >>> s[0]=98

# >>> map(lambda x: x*x ,[1,2,3,4,5])    自己相乘自己
# <map object at 0x10c2c37b8>
# >>> list(map(lambda x: x*x ,[1,2,3,4,5]))
# [1, 4, 9, 16, 25]

# >>> filter(lambda x: x>3,[1,2,3,4,5])
# <filter object at 0x10c2c39b0>
# >>> list(filter(lambda x: x>3,[1,2,3,4,5]))
# [4, 5]

# >>> import functools
# >>> functools.reduce(lambda x,y:x+y,[1,2,4,5,6,7,8,4,5,1])
# 43
# >>> functools.reduce(lambda x,y:x*y,[1,2,4,5,6,7,8,4,5,1])
# 268800
# >>> functools.reduce(lambda x,y:x*y,[1,2,4,5,6,7,8,4,5,1],3)
# 806400
#


# >>> s = 'hey ,my name is alex\n, fro m shandong'
# >>> print(s)
# hey ,my name is alex
# , fro m shandong
# >>> print(s,end=',')
# hey ,my name is alex
# , fro m shandong,>>>
# >>> print('heifeng','gangniang',sep='->')
# heifeng->gangniang
# >>>

# msg = "又回到最初的起点"
# f = open("print_tofile","w" )
# print(msg,"记忆中你青涩的脸",sep="|",end="",file=f)
# print(msg,"记忆中你青涩的脸",sep="|",end="",file=f)
#

# tuple       元组

# >>> def  f():
# ...     pass
# ...
# >>> f
# <function f at 0x10d9f5ea0>
# >>> callable(f)      用来判断一个变量是不是函数 可以使用
# True
callable(a)  这个对像可以调用不 判断
False

# >>> s = {1,2,3,4,5,5}
# >>> s.discard(3)
# >>> s
# {1, 2, 4, 5}
# >>> s=frozenset(s)
# >>> s.difference()
# frozenset({1, 2, 4, 5})



 # >>> vars()  打印出来变量名  变量名和对应变量值


# >>> locals()  在函数里面运行，打印当前函数局部变量  局部变量
#  >>> def f():
# ...     n = 3
# ...     print(locals())
# ...
# >>> f()
# {'n': 3}

# globals()   全局变量

# >>> a = [1,3,4,]
# >>> b = ['a','b','c','d']
# >>> zip(a)
# <zip object at 0x1086f5c08>
# >>> list(zip(a,b))     一一对应，多的丢弃
# [(1, 'a'), (3, 'b'), (4, 'c')]


# >>> round(1.3345677)
# 1
# >>> round(1.3345677,)
# 1
# >>> round(1.3345677,2)
# 1.33


# >>> set()   集合
# set()
"""
import  operator
