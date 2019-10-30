#!/usr/bin/env  python3
# coding utf-8

"""
放射 通过字符串映射到对象的属性

"""
'''
class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def talk(self):
        print('%s is talking' % self.name)


obj = People('egon',18)

# print(obj.name)  # obj.__dict__['name']
# print(obj.age)  # obj.__dict__['age']
# choice = input('>>:')  # choice = 'name'
# print(obj.choice)  # print(obj.'name')


# hasattr(obj,'name') # 判断有没有 obj.name  #  obj.__dict__['name']
# print(hasattr(obj,'name'))  # True

# print(getattr(obj,'name',None))
# # print(getattr(obj,'talk',None))

# setattr(obj,'sex','male') # obj.sex='male
# print(obj.sex)

# delattr(obj,'age') # del  obj.age
# print(obj.__dict__)

print(getattr(People,'conuty')) # People。county

'''


class Service:
    def run(self):
        while True:
            inp = input('>>>:').strip() # cmd = 'get a.txt'
            cmds  = inp.split()  # cmds = ['get','a.txt']
            # if hasattr(self,cmds[0]):
            #     func = getattr(self,cmd[0])
            #     func()
            # print(cmds)
            if hasattr(self,cmds[0]):
                func = getattr(self,cmds[0])
                func(cmds)


    def get(self,cmds):
        print('get ....',cmds)


    def put(self,cmds):
        print('put ...',cmds)


obj = Service()
obj.run()