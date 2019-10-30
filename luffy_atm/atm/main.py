#!/usr/bin/env python
#_*_coding:utf-8_*_


from luffy_atm.atm.auth import  authenticate
from luffy_atm.atm.utils import print_error
from luffy_atm.atm.logger import logger
from luffy_atm.atm import logics


transaction_logger = logger("transaction")               # 负责交易 日志
access_logger = logger("access")                         # 记录操作 日志

features = [
    ('账户信息', logics.view_account_info),
    ('取现',logics.with_draw),
    ('还款',logics.pay_bak),
]


def controller(user_obj):
    '''功能分配'''
    while True:
        # print(features)
        for index, feature in enumerate(features):
            print(index,feature[0])
        choice = input("ATM>>>>:")
        if not choice:continue
        if choice.isdigit():
            choice = int(choice)
            if choice < len(features) and choice >= 0:
                features[choice][1](user_obj,transaction_logger=transaction_logger,access_logger=access_logger)
            if choice == 9:
                exit("Bye ！")


def entrance():

    '''ATM程序交互入口'''

    user_obj = {
        'is_authenticated': False ,  # 用户是否认证
        'data':None                  #
    }
    retry_count = 0
    while user_obj['is_authenticated'] is not  True:  # 如果没有认证是False   让用户去登录认证
        account = input("\033[32;Imaccount:\033[0m").strip()
        password = input("\033[32;impassword:\033[0m").strip()

        auth_data = authenticate(account,password)                  # 验证函数

        if auth_data:   # not None means passed  the authenticon
            '''获取到用户数据 auth_data'''
            user_obj['is_authenticated'] = True    # 把改成True 以为其他的函数可以通过user_obj 字典检查用户是否登录
            user_obj['data'] = auth_data

            print("welcome")

            access_logger.info( "user %s just logged in" % user_obj['data']['id'])
            # print(user_obj['data']['id'])
            controller(user_obj)

        else:
            print_error("Wrong username or pasword!")
        retry_count += 1

        if retry_count == 1:
            msg = "user %s tried  wrong password reched 3 times" % account
            print_error(msg)
            access_logger.info(msg)
            break
