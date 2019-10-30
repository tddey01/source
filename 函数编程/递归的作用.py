#!/usr/bin/env  python3
# coding utf-8
"""
递归特性
必须有一个明确的结束条件
每次进入更深一层递归时，问题规模相比上次递归都应有所减少
递归效率不高，递归层次过多会导致栈益出（在计算中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用栈就会加一层栈帧，每当函数返回，栈就会减少一层栈帧，由于栈的大小不是无限的，所以递归调用的次数过多吗，会导致栈益出）

"""
'''
def calc(n):
    print(n)
    if int(n/2) == 0:
        return  n
    return  calc(int(n/2))

calc(10)
'''
"""

def calc(n):
    v = int(n/2)
    print(v)
    if v ==0:
        return  'Done'
    calc(v)

calc(10)
"""
# def calc(n):
#     v = int(n/2)
#     print(v)
#     if v >0:
#         # return  'Done'
#         calc(v)
#     print(n)
#
# calc(10)
#n! = n * (n-1)!
def factorial(n):
    if n ==1:
        return  1
    return  n *  factorial(n -1)


factorial(4)