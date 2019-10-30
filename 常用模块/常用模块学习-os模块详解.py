#!/usr/bin/env python
#_*_coding:utf8 _*_
'''
os 模块提供了很多允许你的程序与操作系统直接交互的功能

得到当前工作目录，即当前Python脚本工作的目录路径: os.getcwd()
返回指定目录下的所有文件和目录名:os.listdir()
函数用来删除一个文件:os.remove()
删除多个目录：os.removedirs（r“c：\python”）
检验给出的路径是否是一个文件：os.path.isfile()
检验给出的路径是否是一个目录：os.path.isdir()
判断是否是绝对路径：os.path.isabs()
检验给出的路径是否真地存:os.path.exists()
返回一个路径的目录名和文件名:os.path.split()     e.g os.path.split('/home/swaroop/byte/code/poem.txt') 结果：('/home/swaroop/byte/code', 'poem.txt')
分离扩展名：os.path.splitext()       e.g  os.path.splitext('/usr/local/test.py')    结果：('/usr/local/test', '.py')
获取路径名：os.path.dirname()
获得绝对路径: os.path.abspath()
获取文件名：os.path.basename()
运行shell命令: os.system()
读取操作系统环境变量HOME的值:os.getenv("HOME")
返回操作系统所有的环境变量： os.environ
设置系统环境变量，仅程序运行时有效：os.environ.setdefault('HOME','/home/alex')
给出当前平台使用的行终止符:os.linesep    Windows使用'\r\n'，Linux and MAC使用'\n'
指示你正在使用的平台：os.name       对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'
重命名：os.rename（old， new）
创建多级目录：os.makedirs（r“c：\python\test”）
创建单个目录：os.mkdir（“test”）
获取文件属性：os.stat（file）
修改文件权限与时间戳：os.chmod（file）
获取文件大小：os.path.getsize（filename）
结合目录名与文件名：os.path.join(dir,filename)
改变工作目录到dirname: os.chdir(dirname)
获取当前终端的大小: os.get_terminal_size()
杀死进程: os.kill(10884,signal.SIGKILL)
'''

import os
# print(os.getcwd()) #得到当前工作目录
# print(os.listdir())    #返回指定目录下的所有文件和目录名
# print(os.system('ipconfig'))  #运行系统命令
# print(os.getenv('HOME'))  #读取操作系统环境变量HOME的值
# print(os.environ)  #返回操作系统所有的环境变量
# print(os.environ.setdefault('TEST','66'))   #设置系统环境变量，仅程序运行时有效
# print(os.name)  #指示你正在使用的平台：os.name       对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'
# print(os.makedirs('test/ss/s/'))  #递归创建多级目录
# print(os.removedirs('test/ss/s'))   #删除多个目录
# print(os.stat('my_module.py'))
'''
os.stat_result(
st_mode=33206            # 权限模式
st_ino=1337976690656     # 节点号   
st_dev=3760966475        # 驻留的设备
st_nlink=1               # 的链接数。
st_uid=0                 # 所有用户的user id
st_gid=0                 # 所有用户的group id
st_size=161              # 文件的大小，以位为单位
st_atime=1553689446      # 文件最后访问时间
st_mtime=1553689446      # 文件最后修改时间
st_ctime=1553689218)     # 文件创建时间
'''
# print(os.path.join('root','test','t.py'))
# print(os.path.join('root','test','t.py'))
# 'root/test/t.py'
# >>> os.get_terminal_size()
# os.terminal_size(columns=233, lines=65)

"""
信号 值 处理动作 发出信号的原因 
---------------------------------------------------------------------- 
SIGHUP 1 A 终端挂起或者控制进程终止 
SIGINT 2 A 键盘中断（如break键被按下） 
SIGQUIT 3 C 键盘的退出键被按下 
SIGILL 4 C 非法指令 
SIGABRT 6 C 由abort(3)发出的退出指令 
SIGFPE 8 C 浮点异常 
SIGKILL 9 AEF Kill信号 
SIGSEGV 11 C 无效的内存引用 
SIGPIPE 13 A 管道破裂: 写一个没有读端口的管道 
SIGALRM 14 A 由alarm(2)发出的信号 
SIGTERM 15 A 终止信号 
SIGUSR1 30,10,16 A 用户自定义信号1 
SIGUSR2 31,12,17 A 用户自定义信号2 
SIGCHLD 20,17,18 B 子进程结束信号 
SIGCONT 19,18,25 进程继续（曾被停止的进程） 
SIGSTOP 17,19,23 DEF 终止进程 
SIGTSTP 18,20,24 D 控制终端（tty）上按下停止键 
SIGTTIN 21,21,26 D 后台进程企图从控制终端读 
SIGTTOU 22,22,27 D 后台进程企图从控制终端写 

下面的信号没在POSIX.1中列出，而在SUSv2列出 

信号 值 处理动作 发出信号的原因 
-------------------------------------------------------------------- 
SIGBUS 10,7,10 C 总线错误(错误的内存访问) 
SIGPOLL A Sys V定义的Pollable事件，与SIGIO同义 
SIGPROF 27,27,29 A Profiling定时器到 
SIGSYS 12,-,12 C 无效的系统调用 (SVID) 
SIGTRAP 5 C 跟踪/断点捕获 
SIGURG 16,23,21 B Socket出现紧急条件(4.2 BSD) 
SIGVTALRM 26,26,28 A 实际时间报警时钟信号(4.2 BSD) 
SIGXCPU 24,24,30 C 超出设定的CPU时间限制(4.2 BSD) 
SIGXFSZ 25,25,31 C 超出设定的文件大小限制(4.2 BSD) 
"""
import signal

# print(os.kill(2765,signal.SIGKILL)) #杀死进程
# print(os.kill(2765,signal.SIGTERM)) #杀死进程