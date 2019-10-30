#!/usr/bin/env  python3
# coding utf-8

# from gevent import monkey;monkey.patch_all()
#
# import gevent
# import time
#
# def eat(name):
#     print('%s eat1 '%name)
#     gevent.sleep(3)
#     print('%s eat 2 ' %name)
#
#
# def play(name):
#     print('%s play 1 '%name)
#     gevent.sleep(5)
#     print('%s play 2 ' %name)
#
# start_time = time.time()
# g1 = gevent.spawn(eat,'egon')
# g2 = gevent.spawn(play,'alex')
#
# g1.join()
# g2.join()
#
# stop_time = time.time()
# print(stop_time - start_time)


from gevent import monkey;monkey.patch_all()
import gevent
import time

def eat(name):
    print('%s eat1 '%name)
    gevent.sleep(3)
    print('%s eat 2 ' %name)


def play(name):
    print('%s play 1 '%name)
    gevent.sleep(5)
    print('%s play 2 ' %name)


g1 = gevent.spawn(eat,'egon')
g2 = gevent.spawn(play,'alex')

gevent.joinall([g1,g2])



