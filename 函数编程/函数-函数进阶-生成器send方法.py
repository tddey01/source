#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
函数有了yield之后
    1 函数名加()就变得到了一个生成器
     return 在生成器里，代表 生成器的终止，直接 报错

next()
    唤醒 生成器并继续 执行
send('stop')
     唤醒并发送执行
     发送一个信息到生成 器内部
"""

def  range2 (n):

    count = 0
    while count < n:
        print('count',count)
        count += 1
        sign =  yield  count
        if  sign == None:
        # if sign == "stop":
            print('---sigin--', sign)
            break

    return 3333              #生成奇异常，结束 抛出异常  3333
new_range = range2(10)
n1 = next(new_range)
print('do sth else...')
new_range.send(None)
# new_range.send("stop")
#send('stop')
# 唤醒并发送执行
#  发送一个信息到生成 器内部


