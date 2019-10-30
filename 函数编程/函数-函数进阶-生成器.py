#!/usr/bin/env python
# -*- coding: utf-8 -*-
# a = [i for i in range(1000)]
# print(a)

# a2 = (i for  i in range(1000))
# print(next(a2))
# print(next(a2))
# print(next(a2))
#
# for i in (i for  i in range(5)):
#     print(i)

# a3 = (i for  i in  range(5))
#
# # for  i in a3:
# #     print(i)
# #
# # while True:
# #     print(next(a3))
#
# print(range(100))  #生成器


# def fib(max):
#     n,a,b = 0, 0, 1
#     while n <max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
# fib(15)
#
# def fib1(max):
#     n,a,b = 0, 0, 1
#     while n < max:
#         # print('okk yield')
#         yield  b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
# f = fib1(15)  #turn  function into a generator
#
# #
# # for  i in f:
# #     print(i)
# next(f)  #first  time call next()
# next(f)
'''
#函数-函数进阶-生成器调用方法
a  = (i for i in range(10))

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
'''


# print(range(10))
# print(list(range(10)))

''''
python 2  
    range = list
    xrange  = 生成器
python3  
    range = 生成器
    xrange = 没有
'''