#!/usr/bin/env  python3
# coding utf-8
'''
二 GIL介绍
GIL本质就是一把互斥锁，既然是互斥锁，所有互斥锁的本质都一样，都是将并发运行变成串行，以此来控制同一时间内共享数据只能被一个任务所修改，进而保证数据安全。

可以肯定的一点是：保护不同的数据的安全，就应该加不同的锁。

要想了解GIL，首先确定一点：每次执行python程序，都会产生一个独立的进程。例如python test.py，python aaa.py，python bbb.py会产生3个不同的python进程
'''
