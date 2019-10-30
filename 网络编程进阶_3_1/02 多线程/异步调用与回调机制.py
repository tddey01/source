#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-
"""
# 提交任务两种方式
# 同步调用
# 异步调用
"""
'''
# 同步调用 提交完任务后，就在原地等待任务执行完毕，拿到结果, 在执行下一行代码  导致是程序是串行执行

from  concurrent.futures import ThreadPoolExecutor
import time,random

def  la(name):
    print('%s is running '%name)
    time.sleep(random.randint(3,5))
    res = random.randint(7,13)* '#'
    return {'name':name,'res':res}

def weigh(shit):
    name = shit['name']
    size = len(shit['res'])
    print('%s 拉了<%s>kg'%(name,size))

if __name__ == '__main__':
    pool = ThreadPoolExecutor(13)

    shit1 = pool.submit(la,'alex').result()
    weigh(shit1)

    shit2 = pool.submit(la, 'agoe').result()
    weigh(shit2)

    shit3 = pool.submit(la, 'lsir').result()
    weigh(shit3)
'''

# 异步调用 提交完任务后，不在原地等待任务执行完毕,

from  concurrent.futures import ThreadPoolExecutor
import time,random

def  la(name):
    print('%s is running '%name)
    time.sleep(random.randint(3,5))
    res = random.randint(7,13)* '#'
    return {'name':name,'res':res}


def weigh(shit):
    shit = shit.result()
    name = shit['name']
    size = len(shit['res'])
    print('%s 拉了<%s>kg'%(name,size))

if __name__ == '__main__':
    pool = ThreadPoolExecutor(13)

    pool.submit(la,'alex').add_done_callback(weigh)
    pool.submit(la, 'agoe').add_done_callback(weigh)
    pool.submit(la, 'lsir').add_done_callback(weigh)
