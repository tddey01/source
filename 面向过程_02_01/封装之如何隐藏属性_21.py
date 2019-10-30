#!/usr/bin/env  python3
# coding utf-8
"""
引子
从封装本身的意思去理解，封装就好像是拿来一个麻袋，把小猫，小狗，小王八，还有alex一起装进麻袋，然后把麻袋封上口子。照这种逻辑看，封装=‘隐藏’，
这种理解是相当片面的

先看如何隐藏
在python中用双下划线开头的方式将属性隐藏起来（设置成私有的）

#其实这仅仅这是一种变形操作
#类中所有双下划线开头的名称如__x都会自动变形成：_类名__x的形式：

class A:
    __N=0 #类的数据属性就应该是共享的,但是语法上是可以把类的数据属性设置成私有的如__N,会变形为_A__N
    def __init__(self):
        self.__X=10 #变形为self._A__X
    def __foo(self): #变形为_A__foo
        print('from A')
    def bar(self):
        self.__foo() #只有在类内部才可以通过__foo的形式访问到.

#A._A__N是可以访问到的，即这种操作并不是严格意义上的限制外部访问，仅仅只是一种语法意义上的变形

这种自动变形的特点：

类中定义的__x只能在内部使用，如self.__x，引用的就是变形的结果。
这种变形其实正是针对外部的变形，在外部是无法通过__x这个名字访问到的。
在子类定义的__x不会覆盖在父类定义的__x，因为子类中变形成了：_子类名__x,而父类中变形成了：_父类名__x，即双下滑线开头的属性在继承给子类时
，子类是无法覆盖的。
这种变形需要注意的问题是：

1、这种机制也并没有真正意义上限制我们从外部直接访问属性，知道了类名和属性名就可以拼出名字：_类名__属性，然后就可以访问了，如a._A__N

2、变形的过程只在类的定义是发生一次,在定义后的赋值操作，不会变形



"""


class  A:
    __x = 1   # 在方法前面加两个杠杠下划线  隐藏 变形操作

    def __init__(self,name):
        self.__name = name   # self.__A__name=name

    def __foo(self):  # A.__foo  # def _A__foo(self)
        print('run foo')

    def bar(self):
        self.__foo()
        print('run __foo')

# print(A.__dict__)
# print(A.__x)
# print(A.__foo)
#
# a = A('egon')
# a._A__foo()  # 可以这种方法调用
# print(a.__name)  # a.__dict__['__name']
# print(a.__dict__)
# a.bar()

'''
这种变形的特点
        1 在类外部无法直接obj.__AttrName
        2 在内部是可以直接使用：obj.__AttrName
        3  子类无法覆盖父类__开头的属性
'''

class  Foo:
    def  func(self):
        print('from  Foo')


class Bar(Foo):
    def  func(self):
        print('from  bar')

b = Bar()
b.func()