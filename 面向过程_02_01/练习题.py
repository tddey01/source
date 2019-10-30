#!/usr/bin/env  python3
# coding utf-8
# 练习一：在元类中控制把自定义类的数据属性都变成大写

class Mymetaclass(type):
    def __new__(cls,name,bases,attrs):
        update_attrs={}
        for k,v in attrs.items():
            if not callable(v) and not k.startswith('__'):
                update_attrs[k.upper()]=v
            else:
                update_attrs[k]=v
        return type.__new__(cls,name,bases,update_attrs)

class Chinese(metaclass=Mymetaclass):
    country='China'
    tag='Legend of the Dragon' #龙的传人
    def walk(self):
        print('%s is walking' %self.name)


print(Chinese.__dict__)
'''
{'__module__': '__main__',
 'COUNTRY': 'China', 
 'TAG': 'Legend of the Dragon',
 'walk': <function Chinese.walk at 0x0000000001E7B950>,
 '__dict__': <attribute '__dict__' of 'Chinese' objects>,                                         
 '__weakref__': <attribute '__weakref__' of 'Chinese' objects>,
 '__doc__': None}
'''


#练习二：在元类中控制自定义的类无需init方法

# 1.元类帮其完成创建对象，以及初始化操作；
#　　2.要求实例化时传参必须为关键字形式，否则抛出异常TypeError: must use keyword argument
#　　3.key作为用户自定义类产生对象的属性，且所有属性变成大写

class Mymetaclass(type):
    # def __new__(cls,name,bases,attrs):
    #     update_attrs={}
    #     for k,v in attrs.items():
    #         if not callable(v) and not k.startswith('__'):
    #             update_attrs[k.upper()]=v
    #         else:
    #             update_attrs[k]=v
    #     return type.__new__(cls,name,bases,update_attrs)

    def __call__(self, *args, **kwargs):
        if args:
            raise TypeError('must use keyword argument for key function')
        obj = object.__new__(self) #创建对象，self为类Foo

        for k,v in kwargs.items():
            obj.__dict__[k.upper()]=v
        return obj

class Chinese(metaclass=Mymetaclass):
    country='China'
    tag='Legend of the Dragon' #龙的传人
    def walk(self):
        print('%s is walking' %self.name)


p=Chinese(name='egon',age=18,sex='male')
print(p.__dict__)