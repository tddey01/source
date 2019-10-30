#!/usr/bin/env  python3
# coding utf-8
"""
在类内部定义的函数。分为两大类
    一 绑定方法  绑定给谁  就应该由谁来调用，谁来调用就回把调用者当做第一个参数自动传入
        绑定到对象的方法   在类内定义的没有被任何装饰器修饰的

        绑定到类的方法  在类内定义的被装饰器classmethod修饰的方法

    二 非绑定方法   没有自动传值这么一说了 就类重定义的一个普通工具，对象和类都可以使用
        费绑定方法  不与类或者对象绑定

"""

class Foo:

    def __init__(self,name):
        self.name = name

    def tell(self):
        print('名字是%s' %self.name)

    @classmethod # 绑定给类的方法（classmethod）  classmehtod是给类用的，即绑定到类，类在使用时会将类本身当做参数传给类方法的第一个参数（即便是对象来调用也会将类当作第一个参数传入），python为我们内置了函数classmethod来把类中的函数定义成类方法
    def func(cls):  # 默认传入的是类
        print(cls)

    @staticmethod # 装饰的函数即非绑定方法，就是普通函数 不与类或对象绑定，谁都可以调用，没有自动传值效果
    def func1(x,y):
        # return x + y
        print('x+y')



f = Foo('alex')

# print(Foo.tell)
# Foo.tell(f)

# print(f.tell) # <bound method Foo.tell of <__main__.Foo object at 0x10809a2e8>>  绑定方法
# f.tell()

# print(Foo.func)
# Foo.func()
# print(Foo)

# print(Foo.func1)
# print(f.func1)

Foo.func1(1,2)
f.func1(1,2)