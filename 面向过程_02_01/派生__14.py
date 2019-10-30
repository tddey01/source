#!/usr/bin/env  python3
# coding utf-8
"""
派生
当然子类也可以添加自己新的属性或者在自己这里重新定义这些属性（不会影响到父类），需要注意的是，一旦重新定义了自己的属性且与父类重名，那么调用新增的属性时，就以自己为准了。

class Riven(Hero):
    camp='Noxus'
    def attack(self,enemy): #在自己这里定义新的attack,不再使用父类的attack,且不会影响父类
        print('from riven')
    def fly(self): #在自己这里定义新的
        print('%s is flying' %self.nickname)
在子类中，新建的重名的函数属性，在编辑函数内功能的时候，有可能需要重用父类中重名的那个函数功能，应该是用调用普通函数的方式，即：类名.func()，此时就与调用普通函数无异了，因此即便是self参数也要为其传值

class Riven(Hero):
    camp='Noxus'
    def __init__(self,nickname,aggressivity,life_value,skin):
        Hero.__init__(self,nickname,aggressivity,life_value) #调用父类功能
        self.skin=skin #新属性
    def attack(self,enemy): #在自己这里定义新的attack,不再使用父类的attack,且不会影响父类
        Hero.attack(self,enemy) #调用功能
        print('from riven')
    def fly(self): #在自己这里定义新的
        print('%s is flying' %self.nickname)

r1=Riven('锐雯雯',57,200,'比基尼')
r1.fly()
print(r1.skin)

'''
运行结果
锐雯雯 is flying
比基尼

'''

"""


class Hero:

    def __init__(self,nickname,life_value,aggresivity):
        """

        :param nickname:
        :param life_value:
        :param aggresivity:
        """
        self.nickname = nickname
        self.life_value = life_value
        self.aggresivity = aggresivity

    def attack(self,enemy):
        enemy.life_value -= self.aggresivity


class Garen(Hero):
    camp  = 'demacia'

    def attack(self,enemy):
        print('from Garen Class')


class Riven(Hero):
    camp = 'Noxus'


g = Garen('草丛伦',100,30)
r = Riven('锐雯雯',80,50)

# print(g.camp)
# g.attack(r)
# print(r.life_value)

g.attack(r)