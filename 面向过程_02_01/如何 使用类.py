#!/usr/bin/env  python3
# coding utf-8
"""
#定义  一个函数

def func():
    x = 1
    print('>>>>')

func()

"""


# 先定义类
class LuffyStudent:
    school = 'luffycity' #  #数据属性

    def learn(self):   # 函数属性
        print('is learning')

    def eat(self):
        print('si  eating')

    def sleep(self):
        print('is sleeping')

    print('=======')

# 查看类的名称空间
# print(LuffyStudent.__dict__)   #内存空间地址
# print(LuffyStudent.__dict__['school'])
# print(LuffyStudent.__dict__['learn'])


# 查
# print(LuffyStudent.school)  # LuffyStudent.__dict__['school']
# print(LuffyStudent.learn)  # LuffyStudent.__dict__['learn'])

# 增
LuffyStudent.county = 'china'
# print(LuffyStudent.__dict__)
print(LuffyStudent.county)

#删除
del   LuffyStudent.county

# 改
LuffyStudent.school = 'Luffycity'

