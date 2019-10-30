#!/usr/bin/env  python3
# coding utf-8
'''
def sayshi():
    print("Hello, I' m nobody!")


sayshi()
'''
#定义：函数是指将一组语句的集合通过一个名字（函数名）封装起来，要执行这个函数，只需调用函数名即可
#特性：
 # 减减少重复代码
 # 使程序变得可扩展
 # 使程序变得易维护

#下面这段代码
# a,b = 5,8
# c = a**b
# print(c)

#改成函数写
a,b = 5,8
def calc(x,y):
    res = x ** y
    return res
# print(calc(8,9))
# c = calc(a,b)
# print(c)
