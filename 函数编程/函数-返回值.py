#!/usr/bin/env  python3
# coding utf-8
"""
函数外部的代码想要获取函数的执行结果，就可以在函数利用 return 语句把结果返回
"""
def stu_register(name,age,course='PY',country="CN"):
    print("------注册学生信息-------")
    print("姓名:",name)
    print("age:",age)
    print("国籍:",country)
    print("课程:",course)
    if age > 32:
        return  False
    else:
        return  True

registriation_status = stu_register('王山炮',22,course="PY全站开发",country="JP")
if registriation_status:
    print("注册成功")
else:
    print("too old to be a student.")

#注意
#   函数在执行过程中只要遇到 return 语句，就会停止执行并返回结果，so 也可以理解为 return 语句代表着函数结束
#   如果未在函数中执行 return，那这个函数的返回值为 None