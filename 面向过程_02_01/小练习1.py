#!/usr/bin/env  python3
# coding utf-8
'''
练习1  编写一个 学生类，产生一堆学生对象
要求

有一个计算器（属性），统计总共实例了多少对象

'''


class  Student:
    school = 'luffycity'
    count = 0
    def __init__(self,name,age,sex):
        self.Name = name
        self.Age = age
        self.Sex = sex
        # self.count = self.count + 1
        Student.count += 1
    def learn(self):
        print('%s is learing' %self.Name)


stu1 = Student('alex','male',38)  # 调用类 创建对象
stu2 = Student('jingxing','female',78)
stu3 = Student('egon','male',18)

# Student.count
# stu1.count
# stu2.count
# stu3.count

print(Student.count)
print(stu1.count)
print(stu2.count)
print(stu1.__dict__)
print(stu2.__dict__)

