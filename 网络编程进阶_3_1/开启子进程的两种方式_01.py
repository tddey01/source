#!/usr/bin/env  python3
# coding utf-8

# 方式一
"""
from multiprocessing import Process
import time

def task(name):
    print('%s is running' %name)
    time.sleep(3)
    print('%s is running' %name)

if __name__ == '__main':
    '''
    process (targe=task.kwargs={'name':'子进程'})
    '''
    p = Process(target=task,args=('子进程'))
    p.start()

    print('主')
"""

# 方法二
from multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        print('%s is running' %self.name)
        time.sleep(3)
        print('%s is done' %self.name)

if __name__ == '__main__':
    p = MyProcess('ss')
    p.start()

    print('主')

