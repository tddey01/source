#!/usr/bin/env python
# -*- coding: utf-8 -*-

user_status = False  # 用户登录了就把这个改成True


def login(auth_type):  #qq
    def outer(func):
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

        return inner
    return outer

def home():
    print("---首页----")



def america():
    print("----欧美专区----")


def japan():
    print("----日韩专区----")


@login('qq')
def henan(style):
    print("----河南专区----")



henan('3p')
print(henan)

