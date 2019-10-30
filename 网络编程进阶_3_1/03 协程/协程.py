#!/usr/bin/env  python3
# coding utf-8

import time

def  producer():
    g = consumer()
    next(g)
    for i in range(10000):
        g.send(i)


def consumer():
    while True:
        res = yield


start_time=time.time()
producer()
stop_time=time.time()
print(stop_time-start_time)

# 串行

def  producer():
    res = []
    for i in range(10000):
        res.append(i)
    return res


def consumer(res):
    pass


start_time = time.time()
res = producer()
consumer(res)
stop_time = time.time()
print(stop_time - start_time)