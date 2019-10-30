#!/usr/bin/env  python3
# coding utf-8
"""
形参变量
    只有在被调用时才分配内存单元，在调用结束时，即刻释放分配内存单元。以此，形参只在函数内部有效。函数调用结束返回主调用函数后则不能载使用该形参变量
实参
    可以是常量、变量、表达式、函数等，无论实参何种类型的量，在进行函数调用时，他们都必须有确定的值，以便把这些值传给形参。因此应预先用赋值，输入等办法使参数获得确定值
"""
'''
a,b = 5,8
def calc(x,y):    #形参
    res = x ** y
    return res
# print(calc(8,9))
c = calc(a,b)    #实参
print(c)
'''
"""
发现 country 这个参数 基本都是"CN"
就像我们在网站上注册用户，像国籍这种信息，你不填写，默认就会是 中国，这就是通过默认参数实现，把 country 变成默认参数非简单
"""
# def stu_register(name,age,country,course):
#     print("------注册学生信息-------")
#     print("姓名:",name)
#     print("age:",age)
#     print("国籍:",country)
#     print("课程:",course)
#
# stu_register("王山炮",22,"CN","python_devops")
# stu_register("张交春",21,"CN","Linux")
# stu_register("刘老根",25,"CN","C++")

'''
另外，你可能注意到了，在把 country 变成默认参数后，我同时把他的位置移到了最后面，为什么呢？
'''
# def stu1_register(name,age,course,country="CN"):
#     print("------注册学生信息-------")
#     print("姓名:",name)
#     print("age:",age)
#     print("国籍:",country)
#     print("课程:",course)
#
#
# stu1_register("王山炮", 22 ,"python_devops",country="HK")
# stu1_register("张交春", 21, "Linux")
# stu1_register("刘老根", 25, "C++")

def stu2_register(name, age,course,country="CN"):
    print("registerination  info ...")
    print(name,age,country,course)
    # print(name, age, course, country)
stu2_register("刘老根", 25, "C++",country="HK")


#默认参数一定要放在位置参数后面