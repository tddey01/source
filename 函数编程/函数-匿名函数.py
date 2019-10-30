#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
匿名函数
    节省代码量
    开着高级
"""
'''
def calc (x,y):
    return  x*y


lambda  x,y:x*y  #声明一个匿名函数
'''
"""
def calc(x,y):
    if  x<y:
        return  x*y
    else:
        return  x/y


func = lambda s,y:y*s

func1 = lambda  x,y: x*y  if x <y else x/y

print(calc(3,8))
print(func(3,8))
print(func1(7,5))
"""
'''
data = list(range(10))
print(data)
for index,i in enumerate(data):
    data[index] = i*i

print(data)
'''
date = list(range(10))
print(date)
def f2 (n):
    return n*n

print(list(map(f2,date)))
print(list(map(lambda x:x*x,date)))