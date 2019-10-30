#!/usr/bin/env  python3
# coding utf-8
'''
三 定时器
定时器，指定n秒后执行某操作

from threading import Timer

def hello():
    print("hello, world")

t = Timer(1, hello)
t.start()  # after 1 seconds, "hello, world" will be printed
'''

from threading import  Thread,currentThread,Timer
import time,os,sys,random



# def hello(name):
#     print('hello word %s' %name)
#
# t = Timer(5,hello,args=('egon',))
# t.start()

# 验证码
class Code:
    def __init__(self):
        self.make_cache()

    def make_cache(self,interval=5):
        self.cache = self.make_code()
        print(self.cache)
        self.t = Timer(interval ,self.make_code)
        self.t.start()

    def make_code(self,n=4):
        res = ''
        for i in range(n):
            s1 = str(random.randint(0,9))
            s2 = chr(random.randint(65,90))
            res += random.choice([s1,s2])
        return res

    def check(self):
        while True:
            code = input('请输入验证码>>>: ').strip()
            if code.upper() == self.cache:
                print('验证码输入正确')
                self.t.cancel()
                break

# print(make_code())
obj = Code()
# print(obj.make_code())
obj.check()
