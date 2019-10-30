#!/usr/bin/env  python3
# coding utf-8
"""
高阶函数
    变量可以指向函数，函数的参数能接瘦变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
只需要满足以下任意一个条件，即是高阶函数，
    接受一个多个函数作为输入
    return 返回另一个函数

"""

# def calc(x):
#     return  x*x
#
# f = calc
# # f(4)
# print(f(3))
'''
def func(x,y):
    return x + y

def calc(x):
    return x

f = calc(func)
print(f(5,7))
'''

def func2(x,y):
    return  abs(x+y)

print(func2(4,-6))

