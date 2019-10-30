#!/usr/bin/env  python3
# coding utf-8
'''
接口与归一化设计
抽象类
接口与归一化设计
1.什么是接口

hi boy，给我开个查询接口。。。此时的接口指的是：自己提供给使用者来调用自己功能的方式\方法\入口，java中的interface使用如下


'''


import  abc  # 利用abc模块实现抽象类


class   Animal(metaclass=abc.ABCMeta):  # 只能被继承 不能被实例化
    all_type =  'animal'
    @abc.abstractmethod    # 定义抽象方法，无需实现功能

    def run(self):
        pass

    @abc.abstractmethod   # 定义抽象方法，无需实现功能
    def eat(self):
        pass


# animal =  Animal()   # 不能实例化抽象类


class People(Animal):

    def run(self):
        print('people is  pepleing')

    def eat(self):
        print('people is eating')


'''
class People(Animal):

    def run(self):
        print('people is walking')

    def eat(self):
        print('people is eating')

'''


class Pig(Animal):

    def run(self):
        print('people is rpiging')

    def eat(self):
        print('people is eating')


class Dog(Animal):

    def run(self):
        print('people is walking')

    def eat(self):
        print('people is eating')


# peo1 = People()
# pig1 =  Pig()
# dog1 = Dog()
#
#
# peo1.eat()
# pig1.eat()
# dog1.eat()