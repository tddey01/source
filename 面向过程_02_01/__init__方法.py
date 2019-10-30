#!/usr/bin/env  python3
# coding utf-8
# __inir__方法用来为对象定制自己独有的特征

# 先定义类


class LuffyStudent:
    school = 'luffycity'

    def __init__(self,name,sex,age):  # stu1,'lisi','男',13
        self.Name = name  # stu1.Name = 'lisi'
        self.Sex = sex    # stu1.Sex = '男'
        self.Age = age    # stu1.Age  = 19

    def learn(self):
        print('is learning')

    def eat(self):
        print('si  eating')

    def sleep(self):
        print('is sleeping')

# 后产生对象
# 加上__init__方法后 实例化的步骤
# 1 先产生一个空对象
# LuffyStudent.__init__()

# print(LuffyStudent.__init__(stu1,'lisi','男',13))

stu1 = LuffyStudent('lisi','男',13)

# 查看
# print(stu1.__dict__)
# print(stu1.Name)
# print(stu1.Sex)
# print(stu1.Age)

# 改
stu1.Name =  "王小三"
print(stu1.Name)
print(stu1.__dict__)

# 删除
del stu1.Name
print(stu1.__dict__)

#  增加
stu1.class_name = "Python全站开发"
print(stu1.__dict__)


stu2 = LuffyStudent('李三炮','男','38') # LuffyStudent.__init__(stu2,'李三炮','男','38')
print(stu2.__dict__)  #


