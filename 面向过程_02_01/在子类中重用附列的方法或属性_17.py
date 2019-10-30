#!/usr/bin/env  python3
# coding utf-8
'''
在子类中派生出的新的方法中重用父类的方法，有两种实现方式
方法一：  指明道姓（不依赖继承）  即父类名.父类方法()
方法二   super()（以赖继承）
class Vehicle: #定义交通工具类
     Country='China'
     def __init__(self,name,speed,load,power):
         self.name=name
         self.speed=speed
         self.load=load
         self.power=power

     def run(self):
         print('开动啦...')

class Subway(Vehicle): #地铁
    def __init__(self,name,speed,load,power,line):
        Vehicle.__init__(self,name,speed,load,power)
        self.line=line

    def run(self):
        print('地铁%s号线欢迎您' %self.line)
        Vehicle.run(self)

line13=Subway('中国地铁','180m/s','1000人/箱','电',13)
line13.run()
方式二：super()

class Vehicle: #定义交通工具类
     Country='China'
     def __init__(self,name,speed,load,power):
         self.name=name
         self.speed=speed
         self.load=load
         self.power=power

     def run(self):
         print('开动啦...')

class Subway(Vehicle): #地铁
    def __init__(self,name,speed,load,power,line):
        #super(Subway,self) 就相当于实例本身 在python3中super()等同于super(Subway,self)
        super().__init__(name,speed,load,power)
        self.line=line

    def run(self):
        print('地铁%s号线欢迎您' %self.line)
        super(Subway,self).run()

class Mobike(Vehicle):#摩拜单车
    pass

line13=Subway('中国地铁','180m/s','1000人/箱','电',13)
line13.run()
这两种方式的区别是：方式一是跟继承没有关系的，而方式二的super()是依赖于继承的，并且即使没有直接继承关系，super仍然会按照mro继续往后查找

#A没有继承B,但是A内super会基于C.mro()继续往后找
class A:
    def test(self):
        super().test()
class B:
    def test(self):
        print('from B')
class C(A,B):
    pass

c=C()
c.test() #打印结果:from B


print(C.mro())
#[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
'''
"""


class Hero:   # 继承重复调用类
    x = 3
    def __init__(self,nickname,life_value,aggresivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggresivity = aggresivity
    def attack(self,enemy):
        enemy.life_value -= self.aggresivity

class Garen(Hero):
    camp = 'Demacia'

    def attack(self, enemy):
        Hero.attack(self,enemy)  # 指明道姓
        print('from Geren Class')

        # r1.life_value-=g1.aggresivity

class Riven(Hero):
    camp = 'Noxus'




g1 = Garen('草丛伦',100,30)
r1 = Riven('可爱的锐雯雯',80,50)
print(r1.life_value)
g1.attack(r1)
print(r1.life_value)
"""

'''

class Hero:   # 继承重复调用类
    def __init__(self,nickname,life_value,aggresivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggresivity = aggresivity
    def attack(self,enemy):
        enemy.life_value -= self.aggresivity

class Garen(Hero):
    camp = 'Demacia'

    def __init__(self,nickname,life_value,aggresivity,weapon):
        # self.nickname = nickname
        # self.life_value = life_value
        # self.aggresivity = aggresivity
        Hero.__init__(self,nickname,life_value,aggresivity)
        self.weapon = weapon

    def attack(self, enemy):
        Hero.attack(self,enemy)  # 指明道姓
        print('from Geren Class')

        # r1.life_value-=g1.aggresivity


g1 = Garen('草丛伦',100,30,'金箍棒')

print(g1.__dict__)

'''

"""

#  super()（以赖继承）


class Hero:   # 继承重复调用类
    x = 3
    def __init__(self,nickname,life_value,aggresivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggresivity = aggresivity
    def attack(self,enemy):
        enemy.life_value -= self.aggresivity

class Garen(Hero):
    camp = 'Demacia'

    def attack(self, enemy):
        super(Garen,self).attack(enemy) # 依赖继承
        print('from Geren Class')

        # r1.life_value-=g1.aggresivity

class Riven(Hero):
    camp = 'Noxus'




g1 = Garen('草丛伦',100,30)
r1 = Riven('可爱的锐雯雯',80,50)

g1.attack(r1)
print(r1.life_value)


"""

'''

# 指明道姓（不依赖继承）  即父类名.父类方法()


class Hero:   # 继承重复调用类
    def __init__(self,nickname,life_value,aggresivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggresivity = aggresivity
        
    def attack(self,enemy):
        enemy.life_value -= self.aggresivity


class Garen(Hero):
    camp = 'Demacia'

    def __init__(self,nickname,life_value,aggresivity,weapon):

        Hero.__init__(self,nickname,life_value,aggresivity)
        # super(Garen,self).__init__(nickname,life_value,aggresivity)  #   python2 里面这么写
        super().__init__(nickname,life_value,aggresivity)
        self.weapon = weapon

    def attack(self, enemy):
        Hero.attack(self,enemy)  # 指明道姓
        print('from Geren Class')# super(Garen,self).__init__(nickname,life_value,aggresivity)


g1 = Garen('草丛伦',100,30,'金箍棒')

print(g1.__dict__)

'''

class A :
    def f1(self):
        print('from A')
        super().f1()

class B:
    def f1(self):
    # def f2(self):
        print('from B')


class C(A,B):
    pass


print(C.mro())
# [<class '__main__.C'>,
# <class '__main__.A'>,
# <class '__main__.B'>,
# <class 'object'>]

c = C()
c.f1()
