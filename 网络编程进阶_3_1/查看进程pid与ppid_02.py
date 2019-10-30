#!/usr/bin/env  python3
# coding utf-8

from multiprocessing import Process
import   time,os



def task():
    # print('%s is  running' %os.getpid())
    print('%s is  running ,parnt id <%s>' %(os.getpid(),os.getppid()))
    time.sleep(3)
    # print('%s is  done' %os.getpid())
    print('%s is  done ,parnt id <%s>' %(os.getpid(),os.getppid()))

if __name__ == '__main__':
    p = Process(target=task,)
    p.start()

    print('主',os.getpid(),os.getppid())