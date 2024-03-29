#!/usr/bin/env python
#_*_coding:utf-8_*_
"""
使学员掌握sys模块的使用
sys.argv           命令行参数List，第一个元素是程序本身路径
sys.exit(n)        退出程序，正常退出时exit(0)
sys.version        获取Python解释程序的版本信息
sys.maxint         最大的Int值
sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform       返回操作系统平台名称
sys.stdout.write('please:')  #标准输出 , 引出进度条的例子， 注，在py3上不行，可以用print代替
val = sys.stdin.readline()[:-1] #标准输入
sys.getrecursionlimit() #获取最大递归层数
sys.setrecursionlimit(1200) #设置最大递归层数
sys.getdefaultencoding()  #获取解释器默认编码
sys.getfilesystemencoding  #获取内存数据存到文件里的默认编码

"""

import  sys
# print(sys.argv)
# [root@localhost ~]# python3 test.py  run web
# ['test.py', 'run', 'web']
'''
import  sys
print(sys.argv)
sys.exit('bya')
print('333')
[root@localhost ~]# python3 test.py  run web
['test.py', 'run', 'web']
bya
'''
print(sys.maxsize)  #2147483647
print(sys.platform)  #win32
# print(sys.stdout)
print(sys.stdin)