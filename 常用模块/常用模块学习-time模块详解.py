#!/usr/bin/env python
#_*_coding:utf-8_*_
"""
索引（Index）    属性（Attribute）    值（Values）
0     tm_year（年）                 比如2011
1     tm_mon（月）             1 - 12
2     tm_mday（日）                 1 - 31
3     tm_hour（时）                 0 - 23
4     tm_min（分）             0 - 59
5     tm_sec（秒）             0 - 61
6     tm_wday（weekday）            0 - 6（0表示周日）
7     tm_yday（一年中的第几天）    1 - 366
8     tm_isdst（是否是夏令时）            默认为-1

time.struct_time(tm_year=2019, tm_mon=3, tm_mday=31, tm_hour=12, tm_min=15, tm_sec=18, tm_wday=6, tm_yday=90, tm_isdst=0)

time模块的方法
time.localtime([secs])：将一个时间戳转换为当前时区的struct_time。secs参数未提供，则以当前时间为准。
time.gmtime([secs])：和localtime()方法类似，gmtime()方法是将一个时间戳转换为UTC时区（0时区）的struct_time。
time.time()：返回当前时间的时间戳。
time.mktime(t)：将一个struct_time转化为时间戳。
time.sleep(secs)：线程推迟指定的时间运行。单位为秒。
time.asctime([t])：把一个表示时间的元组或者struct_time表示为这种形式：'Sun Oct 1 12:04:38 2017'。如果没有参数，将会将time.localtime()作为参数传入。
time.ctime([secs])：把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。如果参数未给或者为None的时候，将会默认time.time()为参数。它的作用相当于time.asctime(time.localtime(secs))。
time.strftime(format[, t])：把一个代表时间的元组或者struct_time（如由time.localtime()和time.gmtime()返回）转化为格式化的时间字符串。如果t未指定，将传入time.localtime()。
举例：time.strftime("%Y-%m-%d %X", time.localtime()) #输出'2017-10-01 12:14:23'
time.strptime(string[, format])：把一个格式化时间字符串转化为struct_time。实际上它和strftime()是逆操作。


含义	笔记
%a	Locale的缩写工作日名称。
%A	Locale的完整工作日名称。
%b	Locale的缩写月份名称。
%B	Locale的完整月份名称。
%c	Locale的适当日期和时间表示。
%d	十进制数[01,31]。
%H	小时（24小时制）作为十进制数[00,23]。
%I	小时（12小时制）作为十进制数[01,12]。
%j	一年中的一天作为十进制数[001,366]。
%m	月份为十进制数[01,12]。
%M	分数为十进制数[00,59]。
%p	Locale相当于AM或PM。	(1)
%S	其次是十进制数[00,61]。	(2)
%U	一年中的周数（星期日作为一周的第一天）作为十进制数[00,53]。在第一个星期日之前的新年中的所有日子都被认为是在第0周。	(3)
%w	工作日作为十进制数[0（星期日），6]。
%W	一年中的周数（星期一作为一周的第一天）作为十进制数[00,53]。在第一个星期一之前的新年中的所有日子被认为是在第0周。	(3)
%x	Locale的适当日期表示。
%X	Locale的适当时间表示。
%y	没有世纪的年份作为十进制数[00,99]。
%Y	年份以世纪为十进制数。
%z	时区偏移指示与格式+ HHMM或-HHMM形式的UTC / GMT的正或负时差，其中H表示十进制小时数字，M表示小数分钟数字[-23：59，+ 23：59]。
%Z	时区名称（如果不存在时区，则不包含字符）。
"""


'''
import time

print(time.localtime()) #将一个时间戳转换为当前时区的struct_time。secs参数未提供，则以当前时间为准。
print(time.time())    #返回当前时间的时间戳
a = time.localtime()
print('%s-%s-%s %s:%s' %(a.tm_year,a.tm_mon,a.tm_mday,a.tm_hour,a.tm_min))
# print('%s-%s-% s'%(a.tm_year,a.tm_mon,a.tm_mday))

print(time.gmtime())  #和localtime()方法类似，gmtime()方法是将一个时间戳转换为UTC时区（0时区）的struct_time。
print(time.mktime(a))  #将一个struct_time转化为时间戳

print(time.sleep(0))  #线程推迟指定的时间运行。单位为秒。

print(time.asctime())  #把一个表示时间的元组或者struct_time表示为这种形式：'Sun Oct 1 12:04:38 2017'。如果没有参数，将会将time.localtime()作为参数传入。

print(time.ctime())  #把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。如果参数未给或者为None的时候，将会默认time.time()为参数。它的作用相当于time.asctime(time.localtime(secs))

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))    #把一个代表时间的元组或者struct_time（如由time.localtime()和time.gmtime()返回）转化为格式化的时间字符串。如果t未指定，将传入time.localtime()。

#time.strftime('%y %m-%d %H:%M:%S %Z') #只有在系统里面可以使用  linux windows系统不支持


s =time.strftime(format('%Y-%m-%d %H:%M:%S'))
print(s)
s1 = time.strptime(s,'%Y-%m-%d %H:%M:%S')

s12 = time.mktime(s1)
print(s12)
'''