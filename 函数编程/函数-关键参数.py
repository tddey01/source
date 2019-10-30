#!/usr/bin/env  python3
# coding utf-8
"""
关键参数
    正常情况下，给函数传参数要按顺序，不想安顺就可以用关键参数，只需指定参数名（指定了参数名的参数就叫关键参数），但记住一个要求就是，关键参数必须放在位置参数（以位置顺序确定对应关系的参数）之后
"""

def stu1_register(name,age,course='py',country="CN"):
    print("------注册学生信息-------")
    print("姓名:",name)
    print("age:",age)
    print("国籍:",country)
    print("课程:",course)

stu1_register("王山炮", 22,course='Linux',country="HK")
#使用规则
 # 调用可以这样
 # stu1_register("王山炮", 22,course='Linux',country="HK")
 # 但绝不可以这样
 # stu1_register("王山炮", course='Linux',22,country="HK")