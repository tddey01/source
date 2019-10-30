#!/usr/bin/env  python3
# coding utf-8

'''
# 一 死锁现象
# 所谓死锁： 是指两个或两个以上的进程或线程在执行过程中，因争夺资源而造成的一种互相等待的现象，若无外力作用，它们都将无法推进下去。此时称系
# 统处于死锁状态或系统产生了死锁，这些永远在互相等待的进程称为死锁进程，如下就是死锁


from threading import  Thread,Lock
import time

mutexA = Lock()
mutexB = Lock()


class MyThread(Thread):
    def run(self):
        """

        :return:
        """
        self.f1()
        self.f2()

    def  f1(self):
        """

        :return:
        """
        mutexA.acquire()
        print('%s 拿到A锁'%self.name)

        mutexB.acquire()
        print('%s 拿到B锁'%self.name)

        mutexB.release()

        mutexA.release()

    def f2(self):
        mutexB.acquire()
        print('%s 拿到B锁' % self.name)
        time.sleep(0.1)

        mutexA.acquire()
        print('%s 拿到A锁' % self.name)


        mutexA.release()

        mutexB.release()

if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()
'''

'''
# 二 递归锁  可以连续acquire多次，每acquire一次计数器+1，只有计数为0时，才能被抢到acquire
# 解决方法，递归锁，在Python中为了支持在同一线程中多次请求同一资源，python提供了可重入锁RLock。
# 
# 这个RLock内部维护着一个Lock和一个counter变量，counter记录了acquire的次数，从而使得资源可以被多次require。直到一个线程所有的acquire
# 都被release，其他的线程才能获得资源。上面的例子如果使用RLock代替Lock，则不会发生死锁，二者的区别是：递归锁可以连续acquire多次，而互斥锁只能acquire一次
'''
from threading import  Thread,RLock
import time

mutexB = mutexA = RLock()


class MyThread(Thread):
    def run(self):
        """

        :return:
        """
        self.f1()
        self.f2()

    def  f1(self):
        """

        :return:
        """
        mutexA.acquire()
        print('%s 拿到A锁'%self.name)

        mutexB.acquire()
        print('%s 拿到B锁'%self.name)

        mutexB.release()

        mutexA.release()

    def f2(self):
        mutexB.acquire()
        print('%s 拿到B锁' % self.name)
        time.sleep(0.1)

        mutexA.acquire()
        print('%s 拿到A锁' % self.name)


        mutexA.release()

        mutexB.release()

if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()