#!/usr/bin/env  python3
# coding utf-8
"""
itmes 系列
"""
'''

class Foo:
    def __init__(self,name):
        self.name = name

    def __getitem__(self, item):
        # print('getime...')
        print(item)
        return  self.__dict__.get(item)

    def __setitem__(self, key, value):
        # print('setiem ...')
        # print(key,value)
        self.__dict__[key] = value

    def __delitem__(self, key):
        print('delitem ... ')
        print(key)
        # self.__dict__.pop(key)
        self.__dict__[key]


# obj = Foo()
obj = Foo('agon')
# print(obj.__dict__)

# 查看属性
#obj.属性名
# obj['name']

# 设置属性
#obj.sex='male
# obj['sex'] = 'male'
# print(obj.__dict__)
# print(obj.sex)

# 删除属性
# del obj.name #以前使用方式
# del obj['name']
# print(obj.__dict__)
'''

"""

"""
'''
# d = dict({'name':'age'})
# print(isinstance(d,dict))
# print(d)

class People:
    def __init__(self,name,age):

        self.name = name
        self.age = age

    def __str__(self):

        # print('====>>str')

        return  '<name:%s,age:%s> '%(self.name,self.age)



obj = People('age',18)
print(obj)  # res = obj.__str__()
'''

"""
del  方法

"""

# f = open('settings.py')
# f.read()
# f.close()  # 回收操作系统的资源

class Open:
    def __init__(self,filename):
        print('open  file....')
        self.filename = filename

    def  __del__(self):
        print('del ....')  # 回收操作系统资源 self.close()


f = Open('settings.py')
#  del f # f.__del__()
print('-----main-----')  # del  f  # f.__del__()


