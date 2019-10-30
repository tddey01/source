#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""


level = 'L0'
n = 22


def func():
    level = 'L1'
    n = 33
    print(locals())

    def outer():
        n = 44
        level = 'L2'
        print(locals(),n)

        def inner():
            level = 'L3'
            print(locals(),n) #此外打印的n是多少？
        inner()
    outer()


func()

"""
'''
作用于查找顺序
LEGB  

LGGT

LEGB 代表名字查找顺序: locals -> enclosing function -> globals -> __builtins__

locals 是函数内的名字空间，包括局部变量和形参
enclosing 外部嵌套函数的名字空间
globals 全局变量，函数定义所在模块的名字空间
builtins 内置模块的名字空间
'''

n  = 10
def func():
    n = 20
    print('func',n,'1')

    def func2():
        n = 30
        print('func2',n,'2')

        def func3():
            print('func3',n,'3')

        func3()

    func2()

func()
