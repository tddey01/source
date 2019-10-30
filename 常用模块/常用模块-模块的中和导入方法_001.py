#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
使用模块有什么好处？
    最大的好处是大大提高了代码的可维护性。其次，编写代码不必从零开始。当一个模块编写完毕，就可以被其他地方引用。我们在编写程序的时候，
 也经常引用其他模块，包括Python内置的模块和来自第三方的模块。
    使用模块还可以避免函数名和变量名冲突。每个模块有独立的命名空间，因此相同名字的函数和变量完全可以分别存在不同的模块中，所以，我们自己
 在编写模块时，不必考虑名字会与其他模块冲突

模块  好处
    1 提高可用性
    2 可重用
    3 避免函数名和变量冲突

模块分类
    模块分为三种：
         内置标准模块（又称标准库）执行help('modules')查看所有python自带模块列表
        第三方开源模块，可通过pip install 模块名 联网安装
        自定义模块


模块调用
import module   #导入一个模块

from module import xx   #导入单个模块的某个功能

from module.xx.xx import xx as rename     #模块别名

from module.xx.xx import *      #代表所有模块

注意：模块一旦被调用，即相当于执行了另外一个py文件里的代码
"""
# print(help('modules'))
"""
自定义模块
这个最简单， 创建一个.py文件，就可以称之为模块，就可以在另外一个程序里导入
模块查找路径
发现，自己写的模块只能在当前路径下的程序里才能导入，换一个目录再导入自己的模块就报错说找不到了， 这是为什么？

这与导入路径有关
import sys

print(sys.path)
"""
# import  sys   #导入系统sys模块
# sys.path.append('常用模块')
# print(sys.path)
# import my_module
"""
pip命令默认会连接在国外的python官方服务器下载，速度比较慢，你还可以使用国内的豆瓣源，数据会定期同步国外官网，速度快好多
sudo pip install -i http://pypi.douban.com/simple/ alex_sayhi --trusted-host pypi.douban.com   #alex_sayhi是模块名
"""

# import paramiko
# ssh =  paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# ssh.connect('192.168.217.128',22,'root','123456')
#
# stdin, stdout, stderr = ssh.exec_command('ifconfig')
# print(stdout.read())
# ssh.close()