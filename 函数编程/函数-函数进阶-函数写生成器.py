#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
生产器的创建方式
    1 列表   生成  式 ()
    2 函数

    yield  vs  return、
    return  返回 并终止function
    yield  返回 数据， 并冻结当前的执行过程
        next 唤醒冻结的执行过程，并继续执行，直到遇到下一个yield的


"""

# def  range2 (n):
#
#     count = 0
#     while count < n:
#         # print(count)
#         count += 1
#         yield  count   #return 返回值
#
#
# s = range2(10)
# print(range2(10))
#
# print(next(s))
# print(next(s))

""" """
def  range2 (n):

    count = 0
    while count < n:
        print('count',count)
        count += 1
        yield  count   #return 返回值
new_range = range2(10)
r1 = next(new_range)
print(r1)
r2 = next(new_range)
print(r2)
