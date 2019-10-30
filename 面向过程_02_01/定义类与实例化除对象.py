#!/usr/bin/env  python3
# coding utf-8


"""
面向对象 核心就是对象二字  对象就是特征与技能的结合体
优点   可扩展性强
缺点   编程复杂度高
应用场景   用户需求经常变化，互联网引用  游戏  企业内部应用

类就是一系列对象相似的特征与技能结合体
强调 站在不同的角度，得到的分数是不一样的

在现实世界中   一定先有对象  后又类

在程序中      一定得先定义类  后调用列产生对象


站在路费学院角度  大家都是学生

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
            年龄 = 18
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

"""
# 先定义类


class LuffyStudent:
    school = 'luffycity'

    def learn(self):
        print('is learning')

    def eat(self):
        print('si  eating')

    def sleep(self):
        print('is sleeping')


# 后产生对象
stu1 = LuffyStudent()
stu2 = LuffyStudent()
stu3 = LuffyStudent()

print(stu1)
print(stu2)
print(stu3)