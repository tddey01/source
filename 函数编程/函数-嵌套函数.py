#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
嵌套函数
    函数内部可以在次定义函数，
    执行需要被调用

"""
name = 'alex1'
def change_name():
    name = 'alex2'
    def  change_name2():
        name = 'alex3'
        print('第三层打印',name)
    change_name2()  #调用内层函数
    print('第二层打印',name)
change_name()
print('最外层打印',name)