#!/usr/bin/env  python3
# coding utf-8
# f = open('flush_1.txt', 'w')
# f.write('tset1')
# f.write('\nsfet2')
# f.write('\nsfet3')
# f.write('\nsfet4')
# f.write('\nsfet5')
# f.write('\nsfet6')
# f.flush()   #强制刷新缓存到硬盘

# f = open(file='flush_1.txt' ,mode='r')
# s = f.readline()
# s1 = f.readline()
# s2 = f.readline()     #单行读取
# s3 = f.readline()
# print(s)
# print(s1)
# print(s2)
# print(s3)
# f.close()


# f = open(file='flush_1.txt' ,mode='r')
# s = f.readline()
# s1 = f.readline()
# s2 = f.readline()
# s3 = f.readline()
# print(s)
# print(f.tell())  #返回当前文件操作光标位置
# f.close()

# f = open(file='flush_1.txt' ,mode='r')
# s = f.readline()
# print(s)
# print(f.seek(0))  #宝操作文件的光标移动到指定位置   注意 seek 的长度是按照字节计算的，字符编码存每个字符所占的字节长度不一样
# s1 = f.readline()
# print(s1)
# f.close()

# f = open(file='flush_1.txt' ,mode='r+')
# # print(f.read())
# # print(f.tell())
# print(f.truncate(2))    #指定文件长度节段文件  指定长度的话，就从文件开头开始截断指定长度，不指定长度话，就从当前位置到文件尾部的内容全部去掉
#
# f.close()