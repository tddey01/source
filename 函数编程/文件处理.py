#!/usr/bin/env  python3
# coding utf-8
'''
文件操作分为读、写、修改，我们先从度开始学习
s =  open(file='1.txt',mode='r',encoding='gbk')
date  =  s.read()
print(date)
s.close()
'''
"""
file='1.txt' 表示文件路径
mode = 'r'  表示只读（可以修改为其他）
encoding='utf8' 表示将硬盘上的0101010按照utf8的规则去'断句'，再将'断句'后的每一段0101010转换成unicode的01010101，Unicode对照表中有01010101和字符的对应关系
f.read()  表示读取所有内容，内容是已经转换完毕的字符串
f.close() 表示关闭文件
"""