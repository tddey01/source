#!/usr/bin/env  python3
# coding utf-8

"""
什么是特性property

property是一种特殊的属性，访问它时会执行一段功能（函数）然后返回值
例一：BMI指数（bmi是计算而来的，但很明显它听起来像是一个属性而非方法，如果我们将其做成一个属性，更便于理解）
成人的BMI数值：
过轻：低于18.5
正常：18.5-23.9
过重：24-27
肥胖：28-32
非常肥胖, 高于32
体质指数（BMI）=体重（kg）÷身高^2（m）
EX：70kg÷（1.75×1.75）=22.86
"""
'''

class People:
    def __init__(self,name,weight,height):
        self.name = name
        self.weight = weight
        self.height = height

    @property   # property是一种特殊的属性，访问它时会执行一段功能（函数）然后返回值
    def  bmi(self):
        return  self.weight / (self.height ** 2)


p  = People('egon',78,1.75)
# p.bmi = p.weight / (p.height **2)
# print(p.bmi)
print(p.bmi)
'''


class People:
    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        print('getterr')
        return  self.__name

    @name.setter
    def name(self,val):
        print('setterr',val)
        if not isinstance(val,str):
            print('名字必须是字符串类型')
            return
        self.__name = val

    @name.deleter
    def name(self):
        print('deleter')
        print('不允许删除')



p = People('ange')

# print(p.name)
# p.name  # getterr

# p.name="AGES"       # setterr AGES
# print(p.name)

del p.name    # deleter  不允许删除