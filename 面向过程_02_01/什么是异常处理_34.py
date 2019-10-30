#!/usr/bin/env  python3
# coding utf-8

"""
1 什么是异常 异常是错误发生的信号，一旦程序出错，并且程序没有处理这个错误，就会抛出异常  并且程序的运行随之终止

错误分为两种
语法错误  在程序执行前就要立即 改正过来
print('sss')
print(int('sss'))

逻辑错误
在python中不同的异常可以用不同的类型（python中统一了类与类型，类型即类）去标识，一个异常标识一种错误

常见异常

AttributeError 试图访问一个对象没有的树形，比如foo.x，但是foo没有属性x
IOError 输入/输出异常；基本上是无法打开文件
ImportError 无法引入模块或包；基本上是路径问题或名称错误
IndentationError 语法错误（的子类） ；代码没有正确对齐
IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
KeyError 试图访问字典里不存在的键
KeyboardInterrupt Ctrl+C被按下
NameError 使用一个还未被赋予对象的变量
SyntaxError Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
TypeError 传入对象类型与要求的不符合
UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，
导致你以为正在访问它
ValueError 传入一个调用者不期望的值，即使值的类型是正确的

print('sss')
try:
    int('aaa')
except ValueError as e:
    print('ValueError',e)


print('sss')

异常
强调一  对于错误发生的条件如果可以预知的 此时应该用if判断预防异常
"""
# AGE = 10
# age = input('>>>').strip()
# if age.isdigit():
#     age = int(age)
#     if age > AGE:
#         print('太大了')


# 强调二  错误发生的条件如果是不可预知的，此时应该 用异常处理机制 try...except

# try :
#
#     f = open(file='a.txt',mode='r',encoding='utf8')
#     print(next(f),end='')
#     print(next(f),end='')
#     print(next(f),end='')
#     print(next(f),end='')
#     print(next(f),end='')
#     print(next(f),end='')
#
#
#     f.close()
# except IndexError as e:
#     print('IndexError',e)
#
# except StopIteration :
#     print('出错了')


#
# try:
#     print('>>>>1')
#     # name
#     print('>>>>2')
#     l = [1,2,3]
#     l[100]
#     print('>>>>3')
#     d = {}
#     d['name']
#     print('>>>>4')
# except NameError as e:
#     print('---->',e)
# except IndexError as e:
#     print('---->',e)
# except KeyError as e:
#     print('----->' , e)
#
# print('>>>>1')


# 万能异常  Exception
# 多分支  被检测的代码块抛出的异常有多种可能性，并且我们需要针对一种异常类型都定制专门的处理逻辑
# try:
#     print('>>>>1')
#     name
#     print('>>>>2')
#     l = [1,2,3]
#     l[100]
#     print('>>>>3')
#     d = {}
#     d['name']
#     print('>>>>4')
# except NameError as e:
#     print('---->',e)
# except IndexError as e:
#     print('---->',e)
# except KeyError as e:
#     print('----->' , e)
# except Exception as e:
#     print('---->',e)
#
#
# print('>>>>1')

# 多分支  被检测的代码块抛出的异常有多种可能性，
# 并且我们需要针对所有的异常类型都用一种异常类型都定制专门的处理逻辑  #那就是  Exception被

# try:
#     print('>>>>1')
#     # name
#     print('>>>>2')
#     l = [1,2,3]
#     # l[100]
#     print('>>>>3')
#     d = {}
#     d['name']
#     print('>>>>4')
# except NameError as e:
#     print('---->',e)
#
# except IndexError as e:
#     print('---->',e)
#
# except KeyError as e:
#     print('----->' , e)
#
# except Exception as e:
#     print('统一处理方法',e)
#
# else:
#     print('在被检测的代码块没有发生异常时执行')
#
# finally:
#     print('不管被检测的代码块有无发生异常都会执行')
#
# print('>>>>1')


# 无论异常与否,都会执行该模块,通常是进行清理工作
# try :
#
#     f = open(file='a.txt',mode='r',encoding='utf8')
#     print(next(f),end='')
#     print(next(f),end='')
#     print(next(f),end='')
#     print(next(f),end='')
#     print(next(f),end='')
#     print(next(f),end='')
#
#
#
# except StopIteration  as e :
#     print('出错了',e )
#
# finally:
#     f.close()


# 主动触发异常
# class People:
#     def __init__(self,name,age):
#         if not isinstance(name,str):
#             raise  TypeError('名字必须是传入str类型')
#         if not isinstance(age,int):
#             raise TypeError('年龄必须是传入int类型')
#
#         self.name = name
#         self.age = age
#
# p = People('sss',333)


# 自定义异常
class MyException(BaseException):
    def __init__(self,msg):
        super(MyException,self).__init__()
        self.msg = msg

    def __str__(self):
        return  '<%s>' %self.msg

raise  MyException('我自己异常信息类型')  # 输出异常错误信息

'''
#  .断言:assert 条件

info = {}
info['name'] = 'egno'
# info['age'] = 18
print(info)

# if 'name' not in info:
#     raise  KeyError('必须有name这个key')
#
# if 'age' not in info:
#     raise  KeyError('必须有age这个key')
#
# if info['name'] == 'egno'  and  info['age']  > 10 :
#     print('welcome')

assert ('name' in info ) and ('age' in info)
'''