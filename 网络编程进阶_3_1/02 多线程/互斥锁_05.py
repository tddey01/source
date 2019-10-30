#!/usr/bin/env  python3
# coding utf-8

#mutex

from threading import Thread,Lock
import time


n = 100

# def task():
#     global  n
#     temp = n
#     time.sleep(0.1)
#     n = temp-1
#
#
# if __name__ == '__main__':
#     t_l = []
#     for i in range(100):
#         t = Thread(target=task)
#         t_l.append(t)
#         t.start()
#
#     for t in  t_l:
#         t.join()
#
#     print('主线程',n)

def task():
    global  n
    mutex.acquire()
    temp = n
    time.sleep(0.1)
    n = temp-1
    mutex.release()


if __name__ == '__main__':
    mutex = Lock()
    t_l = []
    for i in range(100):
        t = Thread(target=task)
        t_l.append(t)
        t.start()

    for t in  t_l:
        t.join()

    print('主线程',n)