#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
作用域
 在python中 函数就是一个作用一个作用域 （javascript） 局部变量放置在起作用域中
 代码 定义完成后，佐用于已经生，做用于链条向上查找
"""

age = 18
def func1():
    age = 73
    def func2():
        print(age)
    # return  666
    return  func2

val = func1()
print(val)