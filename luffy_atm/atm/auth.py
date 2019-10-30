#!/usr/bin/env python
#_*_coding:utf-8_*_

from luffy_atm.atm.db_handler  import load_account_data
from luffy_atm.atm.utils import print_error


def authenticate(account,password):
    '''对用户信息进行认证 是否合法用户'''

    account_data = load_account_data(account)
    # print(account_data)

    if account_data['status'] == 0: # 等于0 账户加载成功了
        account_data = account_data['data']   # 这个才会用户真正的用户数据加载成功了
        if password ==  account_data['password']:   # 用户认证成功 合法用户登录
            return account_data       # 为什么返回用户数据    把用户数据放在内存里面
        else:
            return  None     # 返回None 用户验证失败
    else:
        print_error(account_data('error'))
        return  None
