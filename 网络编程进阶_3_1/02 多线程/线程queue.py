#!/usr/bin/env  python3
# coding utf-8
"""
一 线程queue
queue is especially useful in threaded programming when information must be exchanged safely between multiple threads.

有三种不同的用法

class queue.Queue(maxsize=0) #队列：先进先出

import queue

q=queue.Queue()
q.put('first')
q.put('second')
q.put('third')

print(q.get())
print(q.get())
print(q.get())



'''
结果(先进先出):
first
second
third
'''
class queue.LifoQueue(maxsize=0) #堆栈：last in fisrt out

import queue

q=queue.LifoQueue()
q.put('first')
q.put('second')
q.put('third')

print(q.get())
print(q.get())
print(q.get())



'''
结果(后进先出):
third
second
first
'''
class queue.PriorityQueue(maxsize=0) #优先级队列：存储数据时可设置优先级的队列

import queue

q=queue.PriorityQueue()
#put进入一个元组,元组的第一个元素是优先级(通常是数字,也可以是非数字之间的比较),数字越小优先级越高
q.put((20,'a'))
q.put((10,'b'))
q.put((30,'c'))

print(q.get())
print(q.get())
print(q.get())



'''
结果(数字越小优先级越高,优先级高的优先出队):
(10, 'b')
(20, 'a')
(30, 'c')
'''
"""

import queue

# q = queue.Queue(3) # 先进先出->队列
#
# q.put('fires')
# q.put(2)
# q.put('third')
# # q.put(4)
# # q.put(4,block=False)
# # q.put(4,block=True,timeout=3)
#
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get(block=False))   #q.get_nowait()
# print(q.get_nowait())

# print(q.get(block=True,timeout=3))

# q = queue.LifoQueue(3)  # 后进先出->堆栈
# q.put('fires')
# q.put(2)
# q.put('third')
#
# print(q.get())
# print(q.get())
# print(q.get())  # 堆栈 就是先吃先拉  后吃进去的 先吐

q = queue.PriorityQueue(3)  # 优先级队列

q.put((10,'one'))
q.put((40,'two'))
q.put((30,'three'))

print(q.get())
print(q.get())
print(q.get())