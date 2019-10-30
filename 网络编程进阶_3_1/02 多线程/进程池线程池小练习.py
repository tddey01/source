#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-

'''
一 进程池与线程池
在刚开始学多进程或多线程时，我们迫不及待地基于多进程或多线程实现并发的套接字通信，然而这种实现方式的致命缺陷是：服务的开启的进程数或线程数都会随着并发的客户端数目地增多而增多，这会对服务端主机带来巨大的压力，甚至于不堪重负而瘫痪，于是我们必须对服务端开启的进程数或线程数加以控制，让机器在一个自己可以承受的范围内运行，这就是进程池或线程池的用途，例如进程池，就是用来存放进程的池子，本质还是基于多进程，只不过是对开启进程的数目加上了限制

介绍

官网：https://docs.python.org/dev/library/concurrent.futures.html

concurrent.futures模块提供了高度封装的异步调用接口
ThreadPoolExecutor：线程池，提供异步调用
ProcessPoolExecutor: 进程池，提供异步调用
Both implement the same interface, which is defined by the abstract Executor class.
基本方法

1、submit(fn, *args, **kwargs)
异步提交任务

2、map(func, *iterables, timeout=None, chunksize=1)
取代for循环submit的操作

3、shutdown(wait=True)
相当于进程池的pool.close()+pool.join()操作
wait=True，等待池内所有任务执行完毕回收完资源后才继续
wait=False，立即返回，并不会等待池内的任务执行完毕
但不管wait参数为何值，整个程序都会等到所有任务执行完毕
submit和map必须在shutdown之前

4、result(timeout=None)
取得结果

5、add_done_callback(fn)
回调函数
'''

from concurrent.futures import  ProcessPoolExecutor,ThreadPoolExecutor
import  requests
import time




def get(url):
    print('GET %s' %url)
    response = requests.get(url)
    time.sleep(0.1)
    return  {'url':url,'content':response.text }


def parse(res):
    res = res.result()
    print('%s parse res is %s' %(res['url'],len(res['content'])))


if __name__ == '__main__':
    urls=[
        'http://www.cnblogs.com/linhaifeng',
        'https://www.python.org',
        'https://www.openstack.org',
        'https://help.github.com',

    ]
    pool = ThreadPoolExecutor(2)

    for  url in urls:
        # pool.submit(get,url).add_done_callback(parse)
        pool.submit(get,url).add_done_callback(parse)
