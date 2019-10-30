#!/usr/bin/env  python3
# coding utf-8
#w+ 读写模式
# ''''
s =  open(file='1.txt',mode='r+',encoding='gbk')
data = s.read()
print(data)


s.write('\n开发者  girl  河北  167 50 13523452233  ')
s.write('\n开发者  ls  sldow2')
s.write('\n开发者  ls  sldow3')
s.write('\n开发者  ls  sldow4')
s.write('\n开发者  ls  sldow5')

s.close()
# '''




# 写读模式
# s = open(file='1.txt',mode='w+',encoding='gbk')
# date = s.read()
# print(date)
#
# s.write('\n开发者  girl   河北  167 50 13523452213')
# s.write('\n开发者  dir    河南  177 51 13523452213')
# s.write('\n开发者  tooch  北京  157 52 13523452213')
# s.write('\n开发者  gls    上海  187 53 13523452213')
# s.write('\n开发者  girl   江苏  147 54 13523452213')
# s.write('\n开发者  gsl    合肥  177 55 13523452213')
#
# s.close()