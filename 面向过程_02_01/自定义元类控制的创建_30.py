#!/usr/bin/env  python3
# coding utf-8

"""

"""

'''
class Mymeta(type):
    def __init__(self,class_name,class_bases,class_dic):
        if not class_name.istitle():
            raise TypeError('类型错误 类名的首字母必须大写')
        # print(class_name)
        # print(class_bases)
        # print(class_dic)

        super(Mymeta,self).__init__(class_name,class_bases,class_dic)


class Chinese(object,metaclass=Mymeta):
    country = "China"   # Chinese = type(....)

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def talk(self):
        print('%s is talking' %self.name)


# Chinese = Mymeta(class_name,class_bases,class_dic)
'''

# class Foo:
#     """
#     注释
#     """
#     pass
#
# print(Foo.__dict__)


class Mymeta(type):
    def __init__(self,class_name,class_bases,class_dic):
        if not class_name.istitle():
            raise TypeError('类型错误 类名的首字母必须大写')
        # print(class_name)
        # print(class_bases)
        # print(class_dic)
        print(class_dic)
        if '__doc__' not in class_dic or not class_dic['__doc__'].strip():
            raise TypeError('必须有注释，且注释不能为空')

        super(Mymeta,self).__init__(class_name,class_bases,class_dic)


class Chinese(object,metaclass=Mymeta):
    '''
    中国人的类
    '''

    country = "China"   # Chinese = type(....)

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def talk(self):
        print('%s is talking' %self.name)
