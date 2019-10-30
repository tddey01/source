#!/usr/bin/env  python3
# coding utf-8
"""
咋现实世界中
    对象1  王二丫
        特征
            学校 = 'luffycity'
            名字 = "王二丫"
            性别 = '女'
            年龄 = 18
        技能
            学习
            吃饭
            睡觉
            对象1  王二丫

     对象2   李三炮
        特征
            学校 = 'luffycity'
            名字 = "李三炮"
            性别 = '男'
            年龄 = 38
        技能
            学习
            吃饭
            睡觉
     对象3   张铁蛋
        特征
            学校 = 'luffycity'
            名字 = "张铁蛋"
            性别 = '男'
            年龄 = 48
        技能
            学习
            吃饭
            睡觉

    总结现实中路费学院的学生
        相似特征
           学校  = 'luffycity'

        相似特征
            学习
            吃饭
            睡觉

"""
# 先定义类

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

stu1 = LuffyStudent('王二丫','女',23)
stu2 = LuffyStudent('李三炮','男',38)
stu3 = LuffyStudent('张铁蛋','男',48)

# print(stu1.__dict__)
# print(stu2.__dict__)
# print(stu1.__dict__)
# 对象  特征与技能的结合体

# 类   类是一系列对象相似的特征与相似的技能结合体


# 类中的数据属性 ： 是所有对象共有的
# print(LuffyStudent.school)
# print(LuffyStudent.school,id(LuffyStudent.school))
# print(stu1.school,id(stu1.school))
# print(stu2.school,id(stu2.school))
# print(stu3.school,id(stu3.school))

# 类中的函数属性 ： 是绑定给对象 ，绑定到不同的对象是不同的绑定方法，对象调用绑定方式时，会把对象本省当当做第一个传入 传给self

# print(LuffyStudent.learn)   # 函数绑定

# stu1.learn()
# stu1.learn(1) # learn(stu1,1)
#
# stu2.learn(2) # learn(stu1,1)
# stu3.learn(3) # learn(stu1,1)


# print(stu1.learn)  # 类的绑定


# stu1.x = 'from stu1'
# LuffyStudent.x = 'from Luffycity class'
print(stu1.__dict__)
print(stu1.x)

