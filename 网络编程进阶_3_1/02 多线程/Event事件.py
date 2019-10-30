#!/usr/bin/env  python3
# coding utf-8

"""
from  threading import  Thread,Event
import time


event = Event ()
# event.wait()
# event.set()


def student(name):
    '''

    :param name:
    :return:
    '''
    print('学生%s 正在听课 '%name)
    event.wait(3) # 可以设置超时时间
    print('学生 %s 课间活动' %name)


def teacher(name):
    print('老师 %s 正在授课' %name)
    time.sleep(7)
    event.set()


if __name__ == '__main__':
    stu1 = Thread(target=student,args=('alex',))
    stu2 = Thread(target=student, args=('wxx',))
    stu3 = Thread(target=student, args=('yss',))
    t1 = Thread(target=teacher,args=('egon',))

    stu1.start()
    stu2.start()
    stu3.start()
    t1.start()
"""

from  threading import  Thread,Event,currentThread
import time


event = Event()


def conn():
    n = 0
    while not event.is_set():
        if n == 3:
            print('%s try many times' %currentThread().getName())
            return
        print('%s try %s' %(currentThread().getName(),n))
        event.wait(0.5)
        n += 1

    print('%s id coonected ' %currentThread().getName())


def check():
    print('%s is checking' %currentThread().getName())
    time.sleep(4)
    event.set()


if __name__ == '__main__':
    for i in range(3):
        t = Thread(target=conn,)
        t.start()
    t = Thread(target=check,)
    t.start()