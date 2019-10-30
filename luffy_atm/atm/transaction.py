#!/usr/bin/env python
#_*_coding:utf-8_*_


from conf import settings
from .db_handler import save_db


def make_transaction(logger,user_obj,tran_type,amount,**kwargs):

    '''
    deal all the user transactions
    :param logger:  acconunt_data: user account_data
    :param user_obj: tran_type: transaction type
    :param tran_type:  amount: transaction_amount
    :param kwargs:  mainy for loggin userge
    :return:
    '''

    amount = float(amount)
    if  tran_type in settings.TEANSACTION_TYPE:

        interest = amount * settings.TEANSACTION_TYPE[tran_type]['interest']   # 算出利息
        old_balance = user_obj['data']['balance']
        if  settings.TEANSACTION_TYPE[tran_type]['action'] == 'plus':
            new_balance = old_balance + amount + interest
        elif settings.TEANSACTION_TYPE[tran_type]['action'] == 'minus':
            new_balance = old_balance - amount - interest
            #check_credit
            if new_balance < 0:
                print('''\033[31;1mYour credit [%s] is not anough for this transaction [-%s] ,your current  balance is [%s] ''' %(user_obj['data']['credit'],(amount + interest ),old_balance))
                return  {'status':1 , 'error':'交易失败，余额不足'}

        user_obj['data']['balance'] = new_balance   # 把新余额存到用户内存账户数据里
        save_db[user_obj]['data']                   # 数据要同时更新到硬盘账户文件

        logger.info("acconut:%s acction:%s amount:%s interest:%s balance:%s" %(user_obj['data']['id'],tran_type,amount,interest,new_balance))

        return  {'status':0,'msg':"交易操作成功"}
    else:
        print("\033[31;1m Transaction type[%s] is not exits!\033[0m" %tran_type)
        return {'status':1,'error':"交易失败，Transaction type[%s] is  nto exits:!" % tran_type}