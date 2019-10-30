#!/usr/bin/env  python3
# coding utf-8
"""

"""

import settings
import hashlib
import time


class People:
    def __init__(self,name,age,sex):
        self.id = self.create_id()
        self.name = name
        self.age = age
        self.sex = sex

    def  tell_info(self):  #绑定到对象发的方法
        print('Name :%s Age :%s  Sex:%s' %(self.name,self.age,self.sex))


    @classmethod
    def from_conf(cls):
        obj = People(
            settings.name,
            settings.age,
            settings.sex
        )
        return obj
    @staticmethod
    def create_id():
        m = hashlib.md5(str(time.time()).encode('utf8'))
        return  m.hexdigest()



# p = People('agen',18,'male')
# 绑定给对象 就应该有对象来调用  自动将对象本省当做第一个参数传入
# p.tell_info()  # tell_info(p)

#  绑定给类 就应该由谁来调用，谁来调用就回把调用者当做第一个参数自动传入

# p = People.from_conf()
# p.tell_info()

# 非绑定方法  不与类或者对象绑定  谁都可以调用，没有自动传值一说

p1 = People('agon1',18,'amel')
print(p1.id)
