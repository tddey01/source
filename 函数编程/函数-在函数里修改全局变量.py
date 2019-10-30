#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
global 修改全局变量 先声明修改变量  实际开发 不建议修改全局变量
"""
name = "Black girl"

def change_name():
    global  name
    name = "黑色姑娘"
    age = 25
    print("在",name,"里面...",id(name))

change_name()

print(name,id(name))