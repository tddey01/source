#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
名称空间
又名name space, 顾名思义就是存放名字的地方，存什么名字呢？举例说明，若变量x=1，1存放于内存中，那名字x存放在哪里呢？名称空间正是存放名字x与1绑定关系的地方

名称空间共3种，分别如下
locals: 是函数内的名称空间，包括局部变量和形参
globals: 全局变量，函数定义所在模块的名字空间
builtins: 内置模块的名字空间
不同变量的作用域不同就是由这个变量所在的命名空间决定的。
作用域即范围
全局范围：全局存活，全局有效
局部范围：临时存活，局部有效
查看作用域方法 globals(),locals()
"""
# 作用域查找顺序
'''

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
'''

x = 1
print(globals())
print(locals())
print(dir(__builtins__)) #内置方法
