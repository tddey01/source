#!/usr/bin/env  python3
# coding utf-8

import sys


class Course:
    def __init__(self,name,price,period,techer):
        self.nme = name
        self.price = price
        self.period = period
        self.techer = techer


class Student:
    operate_list = [
                   ('查看所有课程', 'show_courses'),
                   ('选择课程', 'select_course'),
                   ('查看已选课程', 'check_selected_course'),
                   ('退出', 'exit')]

    def __init__(self,name):
        '''

        :param name
        '''
        self.name = name
        self.courese = []
    def show_courses(self):
        '''

        :return:   查看可以选课程
        '''
        print('查看可以选课程')

    def select_coures(self):
        '''

        :return:   选择课程
        '''
        print('选择课程')

    def check_selected_coures(self):
        '''

        :return:
        '''
        print('查看已选择课程')

    def exit(self):
        exit()


class Manager:
    """

    """
    operate_list = [('创建课程','create_course'),
                   ('创建学生','create_student'),
                   ('查看所有课程','show_courses'),
                   ('查看所有学生','show_students'),
                   ('查看所有学生的选课情况','show_student_course'),
                   ('退出','exit')]

    def __init__(self,name):
        """

        :param name:
        """
        self.name = name

    def create_course(self):
        """

        :return:  创建课程
        """
        print('创建课程')

    def create_student(self):
        """

        :return:  创建学生
        """
        print('创建学生')

    def show_courses(self):
        """

        :return:  查看所有课程
        """
        print('查看所有课程')

    def show_students(self):
        """

        :return:  查看所有学生
        """
        print('查看所有学生')

    def show_student_course(self):
        """

        :return:  查看所有学生的选课情况
        """
        print('查看所有学生的选课情况')

    def exit(self):
        """

        :return:
        """
        exit()
'''
学生 登录就可以选课了
    学生账户了
    有课程


管理员  登录就可以完成以下功能
    学生的账户是管理创建
    课程也应该是管理创建
    
应该先站在管理的角度上来开发
登录
登录必须能够自动识别身份
用户/密码/身份
'''

def login():
    name = input('username:>>>').strip()
    pawd = input('password:>>>').strip()

    with open('userinfo',encoding='utf8') as f:
        for line in f:
            user,pwd,identify = line.strip().split('|')
            if user == name and pawd == pwd:
                return   {'result':True,'name':name,'id':identify}
        else:
            return {'result':False,'name':name}

ret = login()
if ret['result']:
    print('登录成功')
    if hasattr(sys.modules[__name__],ret['id']):
        cls = getattr(sys.modules[__name__],ret['id'])
        obj = cls(ret['name'])
        for  id,item in enumerate(cls.operate_list,1):
            print(id,item[0])
        func_str = cls.operate_list[int(input('>>>').strip()) -1][1]
        print(func_str)
        if hasattr(obj,func_str):
            getattr(obj,func_str)()

else:
    print('登录失败')

    # if ret['id'] == 'Manager':
    #     obj = Manager(ret['name'])
    #     for  id,item in enumerate(Manager.operate_list,1):
    #         print(id,item)
    #         func_str  = Manager.operate_list[int(input('>>>').strip()) -1][1]
    #         if hasattr(obj,func_str):
    #             getattr(obj,func_str)()
