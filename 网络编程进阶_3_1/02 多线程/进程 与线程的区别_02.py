#!/usr/bin/env  python3
# coding utf-8
'''
# 1、开进程的开销远大于开线程


import time
import random
from multiprocessing import Process
from threading import Thread


def piao(name):
    print('%s piaoing' %name)
    time.sleep(random.randrange(1,5))
    print('%s piao end' %name)


if __name__ == '__main__':
    # 实例化得到四个对象
    # p1=Process(target=piao,args=('egon',)) #必须加,号
    p1=Thread(target=piao,args=('egon',)) #必须加,号
    # 调用对象下的方法，开启四个进程
    p1.start()

    print('主线程')


'''

'''
# 2、同一进程内的多个线程共享该进程的地址空间
import time

from multiprocessing import Process
from threading import Thread

n = 100

def task():
    global   n
    n = 0



if __name__ == '__main__':

    # 线程
    # p1=Thread(target=task)
    # p1.start()
    # p1.join()
    # 进程
    p1=Process(target=task)
    p1.start()
    p1.join()
    print('主线程',n)

'''


# 3、瞅一眼pid

# 进程pid

# from multiprocessing import Process,current_process
# from threading import Thread
# import os
#
#
# def task():
#     print(current_process().pid)
#     print('子进程',os.getpid())
#     print('父进程',os.getppid())
#     print('子进程PID %s 父进程PID %s' %(os.getpid(),os.getppid()))
#
# if __name__ == '__main__':
#
#     # 线程
#     # p1=Thread(target=task)
#     # p1.start()
#     # p1.join()
#     # 进程
#     p1=Process(target=task)
#     p1.start()
#
#     print('主线程',current_process().pid)
#     print('主线程1',os.getgid())
#     print('主线程1', os.getppid())


from threading import Thread,current_thread
import os


def task():

    print('子进程PID %s ' %os.getpid())

if __name__ == '__main__':

    # 线程
    p1=Thread(target=task)
    p1.start()

    print('主线程1',os.getpid())
