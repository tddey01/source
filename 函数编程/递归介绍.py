#!/usr/bin/env  python3
# coding utf-8
"""
在函数内部，可以调用其他函数，。如果一个函数在内部调用自身本身，这个函数就是递归函数
"""
'''
import  sys
print(sys.getrecursionlimit())

# sys.setrecursionlimit(1500)  可以修改
def recursion(n):

    print(n)
    recursion(n+1)

# recursion(1)
'''

#默认1000次

"""
"""
def calc(n):
    print(n)
    if int(n/2) == 0:
        return  n
    return  calc(int(n/2))

calc(10)

