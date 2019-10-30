#!/usr/bin/env  python3
# coding utf-8
"""
封装数据属性   明确的区分内外， 控制外部对隐藏属性的操作行为
"""
'''
class People:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def tell_info(self):
        print('Name:<%s> Age:<%s>' %(self.__name,self.__age))

    def set_info(self,name,age):
        if not isinstance(name,str):
            print('名字必须你字符串类型')

            return

        if not isinstance(age,int):
            print('年龄必须是数字类型')

            return

        self.__name = name
        self.__age = age



p = People('egon',18)

# p.tell_info()

# p.set_info('Egon',38)
# p.tell_info()

# p.set_info(123, 38)  # 名字必须你字符串类型 返回结果

p.set_info('Egon', '22')  # 年龄必须是数字类型

'''

# 封装方法  隔离复杂度

# 1 ：封装数据

# 将数据隐藏起来这不是目的。隐藏起来然后对外提供操作该数据的接口，然后我们可以在接口附加上对该数据操作的限制，以此完成对数据属性操作的严格控制。#
# 取款是功能,而这个功能有很多功能组成:插卡、密码认证、输入金额、打印账单、取钱
# 对使用者来说,只需要知道取款这个功能即可,其余功能我们都可以隐藏起来,很明显这么做
# 隔离了复杂度,同时也提升了安全性


class ATM:
    def __card(self):
        print('插卡')

    def __auth(self):
        print('用户认证')

    def __input(self):
        print('输入取款金额')

    def __print_bill(self):
        print('打印账单')

    def __take_money(self):
        print('取款')

    def withdraw(self):
        self.__card()
        self.__auth()
        self.__input()
        self.__print_bill()
        self.__take_money()


a=ATM()
a.withdraw()

#提示：在编程语言里，对外提供的接口（接口可理解为了一个入口），可以是函数，称为接口函数，这与接口的概念还不一样，接口代表一组接口函数的集合体。
