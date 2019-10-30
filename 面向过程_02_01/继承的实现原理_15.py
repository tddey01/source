#!/usr/bin/env  python3
# coding utf-8


"""
继承的实现原理
python到底是如何实现继承的，对于你定义的每一个类，python会计算出一个方法解析顺序(MRO)列表，这个MRO列表就是一个简单的所有基类的线性顺序列表，例如

# >>> F.mro() #等同于F.__mro__
[<class '__main__.F'>, <class '__main__.D'>, <class '__main__.B'>,
<class '__main__.E'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
  为了实现继承,python会在MRO列表上从左到右开始查找基类,直到找到第一个匹配这个属性的类为止。而这个MRO列表的构造是通过一个C3线性化算法来实现的。
我们不去深究这个算法的数学原理,它实际上就是合并所有父类的MRO列表并遵循如下三条准则:

子类会先于父类被检查
多个父类会根据它们在列表中的顺序被检查
如果对下一个类存在两个合法的选择,选择第一个父类

在Java和C#中子类只能继承一个父类，而Python中子类可以同时继承多个父类，如果继承了多个父类，那么属性的查找方式有两种，分别是：深度优先和广度优先

经典类的深度优先查找.png

新式类的广度优先查找.png

"""
# 1 新式类

# 2 经典类

# 在python2中 --> 经典类： 每一个继承object的类,以及 他的自雷 都称之为经典类

# class Foo:
#     pass
#
# class Bar(Foo):
#     pass

# 在python2中 --> 经典类： 每一个继承object的类,以及 他的自雷 都称之为新式类

# class Foo(object):
#     pass
#
# class Bar(Foo):
#     pass

#  在 python3 中  ---》 新式类：  一个类没有继承object类，默认继承object

# class Foo():
#     pass
# print(Foo.__dict__)

# '''

class A(object):
    def test(self):
        print('from A')

class B(A):
    def test(self):
        print('from B')

class C(A):
    def test(self):
        print('from C')

class D(B):
    def test(self):
        print('from D')

class E(C):
    def test(self):
        print('from E')

class F(D,E):
    # def test(self):
    #     print('from F')
    pass
f1=F()
f1.test()
print(F.__mro__) # 只有新式才有这个属性可以查看线性列表，经典类没有这个属性

# 新式类继承顺序:F->D->B->E->C->A
# 经典类继承顺序:F->D->B->A->E->C
# python3中统一都是新式类
# pyhon2中才分新式类与经典类
# '''