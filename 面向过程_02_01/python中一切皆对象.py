#!/usr/bin/env  python3
# coding utf-8
"""
站的角度不同，定义出的类是截然不同的；
现实中的类并不完全等于程序中的类，比如现实中的公司类，在程序中有时需要拆分成部门类，业务类等；
有时为了编程需求，程序中也可能会定义现实中不存在的类，比如策略类，现实中并不存在，但是在程序中却是一个很常见的类。
python中一切皆为对象， 在python3里统一类列与类型的概念


"""
print(type([1,2,3]))
# print(list)


class LuffyStudent:
    school = 'luffycity'

    def __init__(self,name,sex,age):  # stu1,'lisi','男',13
        self.Name = name  # stu1.Name = 'lisi'
        self.Sex = sex    # stu1.Sex = '男'
        self.Age = age    # stu1.Age  = 19

    def learn(self,x):
    # def learn(self):
        # print('%s is  learning'%self.Name)
        print('%s is  learning %s ' % (self.Name,x))

    def eat(self):
        print('si  eating')

    def sleep(self):
        print('is sleeping')


# print(LuffyStudent)

l1 = [1,2,3]  # l = list([1,2,3])
l2 = [] # l = list([1,2,3])

# l1.append(4)  # list .append(l1,4)
list.append(l1,4)

print(list)
