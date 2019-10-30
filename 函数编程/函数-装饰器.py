#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# 封闭：已实现的功能代码块不应该被修改
# 开放：对现有功能的扩展开放

def home():
    print("---首页----")


def america():
    print("----欧美专区----")


def japan():
    print("----日韩专区----")


def henan():
    print("----河南专区----")
"""
'''
user_status = False #用户登录了就把这个改成True

def login():
    _username = "alex" #假装这是DB里存的用户信息
    _password = "123" #假装这是DB里存的用户信息
    global user_status

    if user_status == False:
        username = input("user:")
        password = input("pasword:")

        if username == _username and password == _password:
            print("welcome login....")
            user_status = True
        else:
            print("wrong username or password!")
    else:
        print("用户已登录，验证通过...")

def home():
    print("---首页----")

def america():
    login() #执行前加上验证
    print("----欧美专区----")

def japan():
    print("----日韩专区----")

def henan():
    login() #执行前加上验证
    print("----河南专区----")



# home()
# america()
henan()
'''
"""

user_status = False  # 用户登录了就把这个改成True


def login(func):  # 把要执行的模块从这里传进来
    _username = "alex"  # 假装这是DB里存的用户信息
    _password = "123"  # 假装这是DB里存的用户信息
    global user_status

    if user_status == False:
        username = input("user:")
        password = input("pasword:")

        if username == _username and password == _password:
            print("welcome login....")
            user_status = True
        else:
            print("wrong username or password!")

    if user_status == True:
        func()  # 看这里看这里，只要验证通过了，就调用相应功能


def home():
    print("---首页----")


def america():
    # login() #执行前加上验证
    print("----欧美专区----")


def japan():
    print("----日韩专区----")


def henan():
    # login() #执行前加上验证
    print("----河南专区----")


# home()
# login(america)  # 需要验证就调用 login，把需要验证的功能 当做一个参数传给login
# # home()
# # america()
# login(henan)
home()
america=login(america)  #你在这里相当于把america这个函数替换了
henan=login(henan)
"""
# '''
user_status = False  # 用户登录了就把这个改成True


def login(func):  # 把要执行的模块从这里传进来

    def inner(*args, **kwargs):  # 再定义一层函数
        _username = "alex"  # 假装这是DB里存的用户信息
        _password = "123"  # 假装这是DB里存的用户信息
        global user_status

        if user_status == False:
            username = input("user:")
            password = input("pasword:")

            if username == _username and password == _password:
                print("welcome login....")
                user_status = True

            else:
                print("wrong username or password!")

        if user_status == True:
            func(*args, **kwargs)  # 看这里看这里，只要验证通过了，就调用相应功能

    return inner  # 用户调用login时，只会返回inner的内存地址，下次再调用时加上()才会执行inner函数


def home():
    print("---首页----")


@login
def america():
    print("----欧美专区----")

@login
def japan():
    print("----日韩专区----")


@login
def henan(style):
    '''
    :param style: 喜欢看什么类型的，就传进来
    :return:
    '''
    print("----河南专区----")


home()
# america = login(america) #你在这里相当于把america这个函数替换了
# henan = login(henan)
# henan()
# #那用户调用时依然写
america()
japan()
henan("3p")
# '''