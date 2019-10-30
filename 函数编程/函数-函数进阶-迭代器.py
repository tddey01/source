#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
迭代器
我们已经知道，可以直接作用于for循环的数据类型有以下几种：
一类是集合数据类型，如list、tuple、dict、set、str等；
一类是generator，包括生成器和带yield的generator function。
这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

可以使用isinstance()判断一个对象是否是Iterable对象：

"""
# from collections import Iterable
# Iterable
# <class 'collections.abc.Iterable'>
# isinstance('abc',Iterable)    #对于字符串
# True
# isinstance(100,Iterable)   #不能对于数字
# False

'''
import time
for n in (100000, 200000, 300000, 400000):
    data = b'x'*n
    start = time.time()
    b = data
    while b:
        b = b[1:]
    print('bytes', n, time.time()-start)

for n in (100000, 200000, 300000, 400000):
    data = b'x'*n
    start = time.time()
    b = memoryview(data)
    while b:
        b = b[1:]
    print('memoryview', n, time.time()-start)
'''
"""
而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。

*可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。

可以使用isinstance()判断一个对象是否是Iterator对象：
>>> from collections import Iterator
>>> isinstance((x for x in range(10)), Iterator)
True
>>> isinstance([], Iterator)
False
>>> isinstance({}, Iterator)
False
>>> isinstance('abc', Iterator)
False
在python里面一切皆为对像

生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
把list、dict、str等Iterable变成Iterator可以使用iter()函数：

>>> isinstance(iter([]), Iterator)
True
>>> isinstance(iter('abc'), Iterator)
True


你可能会问，为什么list、dict、str等数据类型不是Iterator？

这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration
错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算
是惰性的，只有在需要返回下一个数据时它才会计算。

Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。


小结

凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

Python3的for循环本质上就是通过不断调用next()函数实现的，例如：

for x in [1, 2, 3, 4, 5]:
    pass
实际上完全等价于：

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
"""
#思路把存储的数据变成[[],[],[],[],[]],每一行为总列表里面的元素列表，然后再一次遍历匹配结果
def all_need():
    global file
    file = open('restaff_table.txt', 'r+', encoding='utf-8')
    f = file.readlines()
    global  data_list
    data_list = []
    for i in f:
        i = i.strip()
        data_list.append(i.split(','))

def rewrite():
    file.seek(0)
    file.truncate()
    for line in data_list:
        str = ','.join(line)
        file2 = open('restaff_table.txt', 'a', encoding='utf-8')
        file2.write(str+'\n')
        file2.close()

def find_info():
    while True:
        choice2 = input("""
(请选择查询序号)：
find name,age from staff_table where age > 22
find * from staff_table where dept = "IT"
find * from staff_table where enroll_date like "2013"
q 退出
>""").strip()
        all_need()
        count = 0
        if choice2 == 'q':
            file.close()
            break
        if choice2 not  in ['1','2','3']:
            print('\033[31m input wrong \033[0m ')
        for i in range(0, len(data_list)):
            if choice2 == '1':
                if int(data_list[i][2]) > 22:
                    data_str = ' '.join(data_list[i][1:3]).strip('\n')
                    print(data_str)
                    count += 1
                    #file.close()
            if choice2 == '2':
                if data_list[i][4] == 'IT':
                    data_str = ' '.join(data_list[i]).strip('\n')
                    print(data_str)
                    count += 1
                    #file.close()
            if choice2 == '3':
                if '2013' in data_list[i][5]:
                    data_str = ' '.join(data_list[i]).strip('\n')
                    print(data_str)
                    count += 1
                    #file.close()
        print("\033[31m 查询结束，符合条件数为 %s \033[0m" %(count))

def add_info():
    count1 = 0
    while True:
        count = 0
        choice3 = input("""
(请选择序号)：
(录入员工信息:)
q 退出
>""").strip()
        if choice3 == '1':
            all_need()
            new_staff_info = input('''
请按如下顺序输入：
name,age,phone,dept,enroll-date
>''').strip()
            new_staff_list = new_staff_info.split(',')
            new_staff_id = str(len(data_list)+1)
            new_staff_list.insert(0,new_staff_id)
            if len(new_staff_list) != 6:
                print('\033[31m 输入信息不完整，请重新输入 \033[0m')
                continue
            else:
                for i in range(0, len(data_list)):
                    if data_list[i][3] == new_staff_list[3]:
                        print('\033[31m 已存入该员工信息！\033[0m')
                        count += 1
                        break
            if count == 0:
                new_staff_str = ','.join(new_staff_list)
                file2 = open('restaff_table.txt', 'a+', encoding='utf-8')
                file2.write('\n'+new_staff_str)
                file2.close()
                count1 += 1
                print(file2,"\033[31m 新添加的员工信息为：%s \033[0m " %(new_staff_list))
        if choice3 not in ['1','q']:
            print('\033[31m 输入有误，请选择 1 或者 q \033[0m')
        if choice3 == 'q':
            print(f,"\033[31m 添加结束，共添加 %s 个员工信息\033[0m" %(count1))
            break

def del_info():
    count = 0
    while True:
        all_need()
        id_list = []
        for index in range(0,len(data_list)):
            id_list.append(data_list[index][0])
        print(f,'\033[31m id的取值范围为\033[0m {id_list}')
        staff_id = input("""        
\033[31m 请输入需要删除的员工id\033[0m
id：delete from staff_table where staff_id = 3
q：退出
>""").strip()
        if staff_id =='q':
            print(f,"\033[31m  删除结束，共删除 %s 个员工 \033[0m" %(count))
            break
        if staff_id not in id_list:
            print('\033[31m  输入无效id \033[0m')
            continue
        for j in reversed(range(0,len(data_list))):

            if data_list[j][0] == staff_id:
                del data_list[j]
                print(f,'\033[31m 已删除id为 %s 的员工信息 \033[0m' % (staff_id))
                rewrite()
        count += 1
def modify_info():
    while True:
        modify = input("""
请选择下列序号：
把所有dept=IT的纪录的dept改成Market
把name=Alex Li的纪录的年龄改成25
q 退出
>""").strip()
        all_need()
        if modify == 'q':
            break

        count = 0
        for i in range(0, len(data_list)):
            if modify == '1':
                if data_list[i][4] == 'IT':
                    data_list[i][4] = 'Market'
                    rewrite()
                    count += 1
            if modify == '2':
                if data_list[i][1] == "Alex Li":
                    data_list[i][2] = '25'
                    rewrite()
                    count += 1

        print(f,"\033[31m共改动{count}处信息\033[0m")
        if modify not in ['1','2','q']:
            print('输入错误，请重新输入')
            continue

#---------------主函数----------------------
print('-----欢迎登陆员工管理系统------')
file1 = open('staff_table.txt', 'r', encoding='utf-8')  # 要去掉空行的文件
file2 = open('restaff_table.txt', 'w', encoding='utf-8')  # 生成没有空行的文件
try:
    for line in file1.readlines():
        if line == '\n':
            line = line.strip("\n")
        file2.write(line)
finally:
    file1.close()
    file2.close()
while True:
    choice = input("""
请选择下列序号：
查询 
增
删
改
q 退出
>""").strip()
    if choice == '1':
        find_info()
    if choice == '2':
        add_info()
    if choice == '3':
        del_info()
    if choice == '4':
        modify_info()
    if choice == 'q':
        exit()