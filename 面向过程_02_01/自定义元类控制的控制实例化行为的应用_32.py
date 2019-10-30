#!/usr/bin/env  python3
# coding utf-8
"""

"""

# 单例模式
# 实现方式一

# class MySQL:
#     __instance = None
#
#     def __init__(self):
#         self.host =  '127.0.0.1'
#         self.port = 3306
#
#     @classmethod
#     def singleton(cls):
#         if not cls.__instance:
#             obj = cls
#             cls.__instance = obj
#         return cls.__instance
#
#     def conn(self):
#         pass
#
#     def  execute(self):
#         pass
#

# obj1 = MySQL()
# obj2 = MySQL()
#
# print(obj1)
# # print(obj2)
# obj1 = MySQL.singleton()
# obj2 = MySQL.singleton()
# print(obj1)
# print(obj2)
# print(obj1 is obj2)



# 实现方式二   元类的方式


class Mymeta(type):

    def __init__(self,class_name,class_bases,class_dic):
        if not class_name.istitle():
            raise TypeError('类型错误 类名的首字母必须大写')

        if '__doc__' not in class_dic or not class_dic['__doc__'].strip():
            raise TypeError('必须有注释，且注释不能为空')

        super(Mymeta,self).__init__(class_name,class_bases,class_dic)
        self.__instance = None

    def __call__(self, *args, **kwargs):  #obj = Chinese('agen',19)
        if not self.__instance:
            obj = object.__new__(self)
            self.__init__(obj)
            self.__instance = obj

class Mysql(object,metaclass=Mymeta):
    '''
    MySQL 数据库
    '''

    def __init__(self):
        self.host =  '127.0.0.1'
        self.port = 3306


    def conn(self):
        pass

    def  execute(self):
        pass



obj1 = Mysql()
obj2 = Mysql()
#
# print(obj1)
print(obj1 is obj2)
