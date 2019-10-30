#!/usr/bin/env  python3
# coding utf-8
# f = open(file='2.txt' ,mode='r+',encoding='utf8')
# f.seek(6)
# f.write('路学飞城')
# f.close()
import  os

f_name = '1.txt'
f_new_name = "%s.new" %f_name


old_str = "肛娘"
new_str = "乔亦菲"

# old_str = "乔亦菲"
# new_str = "肛娘"


f = open(f_name,'r',encoding='utf8')
f_new = open(f_new_name,'w',encoding='utf8')


for line in f:

    if old_str in line:
        line = line.replace(old_str,new_str)  #replace 方法：返回根据正则表达式进行文字替换后的字符串的复制。

    f_new.write(line)

f.close()
f_new.close()

os.rename(f_new_name,f_name)
