#!/usr/bin/env  python3
# coding utf-8
"""
一 知识储备
exec：三个参数

参数一：字符串形式的命令

参数二：全局作用域（字典形式），如果不指定，默认为globals()

参数三：局部作用域（字典形式），如果不指定，默认为locals()



"""
"""
# exec的使用

# 可以把exec命令的执行当成是一个函数的执行，会将执行期间产生的名字存放于局部名称空间中
g={
'x':1,
'y':2
}
l={}

exec('''
global x,z
x=100
z=200

m=300
''',g,l)

print(g) #{'x': 100, 'y': 2,'z':200,......}
print(l) #{'m': 300}
"""
"""
二 引子（类也是对象）
class Foo:
      pass

f1=Foo() #f1是通过Foo类实例化的对象
python中一切皆是对象，类本身也是一个对象，当使用关键字class的时候，python解释器在加载class的时候就会创建一个对象(这里的对象指的是类而非类的实例)，因而我们可以将类当作一个对象去使用，同样满足第一类对象的概念，可以：

把类赋值给一个变量

把类作为函数参数进行传递

把类作为函数的返回值

在运行时动态地创建类

上例可以看出f1是由Foo这个类产生的对象，而Foo本身也是对象，那它又是由哪个类产生的呢？

#type函数可以查看类型，也可以用来查看对象的类，二者是一样的
print(type(f1)) # 输出：<class '__main__.Foo'> 表示，obj 对象由Foo类创建
print(type(Foo)) # 输出：<type 'type'>


一切皆对象 对象可以 怎么用？
1 都可以被引用   x=obj
2  都可以当做函数的参数传入
3 都可以当做函数的返回值 
4 都可以当做容器类的元素 l=[func,time,obj,1]



"""
#  类 也是对象  Foo type(Foo) #  <class 'type'>

'''
class Foo:
    pass

obj = Foo()
print(type(obj))
print(type(Foo))


class Bar:
    pass

print(type(Bar))  # <class 'type'>
'''
"""

# 产生类的类称之为元类， 默认所以用class定义的类，他们的元类是type
#  方式一  class关键字

class Chinese:
    country = "China"   # Chinese = type(....)

    def __init__(self,name,age):
        self.name = name
        self.age = age


    def talk(self):
        print('%s is talking' %self.name)

obj = Chinese('egon',18)
print(obj,obj.name,obj.age)
"""
# 方法二 type
# 定义类的三要素，类名，累的基类，类的名臣空间
class_name = 'Chinese'
class_bases = (object,)

class_body = """
country = "China"   # Chinese = type(....)

def __init__(self,name,age):
   self.name = name
   self.age = age


def talk(self):
     print('%s is talking' %self.name)
"""

class_dic = {}
exec(class_body,globals(),class_dic)
# print(class_dic)

Chinese1 = type(class_name,class_bases,class_dic)

# print(Chinese1)

obj1 = Chinese1('egon',18)
print(obj1,obj1.name,obj1.age)