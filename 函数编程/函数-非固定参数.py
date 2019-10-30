#!/usr/bin/env  python3
# coding utf-8
"""
若你的函数在定义时不确定用户想传入多个参数，就可以使用非固定参数
"""
'''
def stu_register(name,age,*args):  #*args 会把多传入的参数变成一个元祖形式
    print(name,age,args)

stu_register("kevin",22)
#输出
#kevin 22 （）#后面这个（）就是 args，只是因为没有传入值，所以为空

stu_register("kevi",32,"CCN","Python")
#输出
# kevin  32 ('CCN', 'Python')
'''
#非固定关键字参数
"""
def  func(name,*args,**kwargs):  #*kwargs 会把多传入的参数变成一个 dict 形式
    print(name,args,kwargs)

func('keivn',22)
#keivn (22,) {}   #后面这个{}就是 kwargs，只是因为没传值，所以为空

func('alex',22,'sfe',add=500,usm='lisan')
"""
