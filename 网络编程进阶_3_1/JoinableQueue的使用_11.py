#!/usr/bin/env  python3
# coding utf-8
from multiprocessing import Process,JoinableQueue
import  time


def producer(q):
    for i in range(3):
        res = '包子%s' %i
        time.sleep(2)
        print('生产者生产了%s' %res)

        # consumer(res)
        q.put(res)
    q.join()


def consumer(q):
    while True:
        res = q.get()
        if res is  None:break
        time.sleep(0.5)
        print('消费者吃了%s' %res )
        q.task_done()


if __name__ == '__main__':
    # 容器
    q = JoinableQueue()

    # 生产者
    p1=Process(target=producer,args=(q,))

    # 消费者
    c1 = Process(target=consumer,args=(q,))
    c1.daemon = True

    p1.start()
    c1.start()

    p1.join()
    print('主')
