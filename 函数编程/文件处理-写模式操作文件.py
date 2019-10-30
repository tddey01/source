#!/usr/bin/env  python3
# coding utf-8
'''
循环文件
s =  open(file='1.txt',mode='rb')
date  =  s.read()
print(date)
s.close()
'''
"""
s =  open(file='1.txt',mode='r',encoding='gbk')
for line in s:
    print(line)

s.close()


# 每行之间都有空行
"""

# f = open(file='2.txt',mode='w',encoding='gbk')
# f.write('卢雪飞城 ！')
# f.close()

# f = open(file='2.txt',mode='r',encoding='gbk')
# print(f.read())
# f.close()



# f = open('3.txt',mode='wb')
# f.write('刘集村是！'.encode('gbk'))
# f.close()

# f = open('3.txt',mode='r',encoding='gbk')
# print(f.read())
# f.close()

# wb 模式写入文件  r可以直接读取

