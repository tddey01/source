#!/usr/bin/env  python3
# coding utf-8
'''
组合与重用性
软件重用的重要方式除了继承之外还有另外一种方式，即：组合

组合指的是，在一个类中以另外一个类的对象作为数据属性，称为类的组合

# >>> class Equip: #武器装备类
...     def fire(self):
...         print('release Fire skill')
...
# >>> class Riven: #英雄Riven的类,一个英雄需要有装备,因而需要组合Equip类
...     camp='Noxus'
...     def __init__(self,nickname):
...         self.nickname=nickname
...         self.equip=Equip() #用Equip类产生一个装备,赋值给实例的equip属性
...
# >>> r1=Riven('锐雯雯')
# >>> r1.equip.fire() #可以使用组合的类产生的对象所持有的方法
release Fire skill

组合与继承都是有效地利用已有类的资源的重要方式。但是二者的概念和使用场景皆不同，


1.继承的方式

通过继承建立了派生类与基类之间的关系，它是一种'是'的关系，比如白马是马，人是动物。

当类之间有很多相同的功能，提取这些共同的功能做成基类，用继承比较好，比如老师是人，学生是人

2.组合的方式

用组合的方式建立了类与组合的类之间的关系，它是一种‘有’的关系,比如教授有生日，教授教python和linux课程，教授有学生s1、s2、s3...

示例：继承与组合

class People:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

class Course:
    def __init__(self,name,period,price):
        self.name=name
        self.period=period
        self.price=price
    def tell_info(self):
        print('<%s %s %s>' %(self.name,self.period,self.price))

class Teacher(People):
    def __init__(self,name,age,sex,job_title):
        People.__init__(self,name,age,sex)
        self.job_title=job_title
        self.course=[]
        self.students=[]


class Student(People):
    def __init__(self,name,age,sex):
        People.__init__(self,name,age,sex)
        self.course=[]


egon=Teacher('egon',18,'male','沙河霸道金牌讲师')
s1=Student('牛榴弹',18,'female')

python=Course('python','3mons',3000.0)
linux=Course('python','3mons',3000.0)

#为老师egon和学生s1添加课程
egon.course.append(python)
egon.course.append(linux)
s1.course.append(python)

#为老师egon添加学生s1
egon.students.append(s1)


#使用
for obj in egon.course:
    obj.tell_info()
总结：

当类之间有显著不同，并且较小的类是较大的类所需要的组件时，用组合比较好

'''


class People:
    school = 'luffycity'

    def  __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex


class Teacher(People):   # 老师

    # def __init__(self,name,age,sex,level,salary):
    def __init__(self, name, age, sex, level, salary):
        super().__init__(name,age,sex)

        self.level = level
        self.salary = salary

    def teach(self):
        print('%s is  teaching' % self.name)


class Student(People):   # 学生

    # def __init__(self, name, age, sex, class_time):
    def __init__(self, name, age, sex, class_time):
        super().__init__(name,age,sex)

        self.class_time = class_time


    def learn(self):
        print('%s is  learning' % self.name)



class Coures:

    def __init__(self,course_name,coures_price,couse_period):

        self.course_name = course_name
        self.course_price = coures_price
        self.course_period = couse_period

    def tell_info(self):
        print('课程<%s> 课程价格<%s> 课程周期<%s> ' % (self.course_name,self.course_price,self.course_period))


class Date:

    def __init__(self,year,mon,day):
        self.year = year
        self.mon = mon
        self.day = day

    def tell_info(self):
        print('%s-%s-%s'% (self.year,self.mon,self.day))


# teacher1 = Teacher('alex',18,'male',10,3000)   # 老师

# teacher1 = Teacher('alex',18,'male',10,3000,'python',3000,'3mons')   # 老师
# teacher1 = Teacher('agon',18,'male',10,3000,'python',3000,'3mons')   # 老师


# teacher1 = Teacher('agon',18,'male',10,3000)
# python = Coures('python',3000,'3mons')
# linux = Coures('linux',3000,'4mons')
# # print(python.course_name)

# teacher1.coures = python


# print(python)
# print(teacher1.course)
# print(teacher1.course.course_name)

# teacher1.coures.tell_info()

# student1 = Student('zs',28,'female','08:30:00',)  # 学生
# student1.course1 = python
# student1.course2 = linux

# student1.course1.tell_info()
# student1.course2.tell_info()

## student1.courses= []

## student1.courses.append(python)
## student1.courses.append(linux)

student1 = Student('zs',28,'female','08:30:00',)  # 学生
d = Date(1988,4,20)
python = Coures('python',3000,'3mons')

student1.birh=d
student1.birh.tell_info()

student1.course = python

student1.course.tell_info()




