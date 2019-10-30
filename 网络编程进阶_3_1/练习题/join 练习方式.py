#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-

# 1、改写下列程序，分别别实现下述打印效果

'''
from multiprocessing import Process
import time
import random

def task(n):
    time.sleep(random.randint(1,3))
    print('-------->%s' %n)

if __name__ == '__main__':
    p1=Process(target=task,args=(1,))
    p2=Process(target=task,args=(2,))
    p3=Process(target=task,args=(3,))

    p1.start()
    p2.start()
    p3.start()

    print('-------->4')
'''


'''
# 保证最后输出-------->4

from multiprocessing import Process
import time
import random

def task(n):
    time.sleep(random.randint(1,3))
    print('-------->%s' %n)

if __name__ == '__main__':
    p1=Process(target=task,args=(1,))
    p2=Process(target=task,args=(2,))
    p3=Process(target=task,args=(3,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
    print('-------->4')
'''


from multiprocessing import Process
import time
import random

def task(n):
    time.sleep(random.randint(1,3))
    print('-------->%s' %n)

if __name__ == '__main__':
    p1=Process(target=task,args=(1,))
    p2=Process(target=task,args=(2,))
    p3=Process(target=task,args=(3,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
    print('-------->4')