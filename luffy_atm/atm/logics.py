#!/usr/bin/env python
#_*_coding:utf-8_*_


# from .logger import  logger

from luffy_atm.atm.transaction import make_transaction


def view_account_info(account_data,*args,**kwargs):
    '''查看账户信息'''
    # print('view_account_info',account_data,kwargs)
    tran_logger = kwargs.get("transaction_logger")
    # make_transaction()
    print('ACCOUN_INFO'.center(50,'-'))
    for k,v in account_data['data'].items():
        if k  not  in ('password',):
            print('%15s:%s'%(k,v))
    print('END'.center(50,'-'))


def with_draw(account_data, *args,**kwargs):
    '''取现'''
    trans_logger = kwargs.get("transaction_logger")
    current_balance = '''---------------BALNCE INFO------------------
        Credit : %s
        Balance : %s  ''' %(account_data['data']['credit'],account_data['data']['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        withdraw_amount = input("\033[33;1m 请输入取现金额:\033[0m").strip()  # 取得金额 1
        if len(withdraw_amount) >0 and withdraw_amount.isdigit():
            withdraw_amount = int(withdraw_amount)
            if (account_data['data']['balance'] / 2) >= withdraw_amount:
                transacrion_result = make_transaction(trans_logger, account_data,'withdraw_amount',)
                if  transacrion_result('status') == 0:
                    print('''\033:[42;1mNew Balance:%s \033[0m''' %(account_data['data']['balance']))
                else:
                    print("可取现余额不足，可提现%s"%(int(account_data['data']['balance'] / 2) ))

        if  withdraw_amount == 'b':
            back_flag = True


def pay_bak(account_data,*args,**kwargs):
    '''
    还款接口
    :param account_data:
    :param args:
    :param kwargs:
    :return:
    '''
    trans_logger = kwargs.get("transaction_logger")
    current_balance = '''
    --------------------------BALANCE INFO-----------------------------
    Credit :  %s
    Balance  %s 
    ''' %(account_data['data']['credit'],account_data['data']['balance'])
    print(current_balance)
    pay_amount = input("\033[33;1m请输入还款金额：\033[0m").strip()
    if len(pay_amount) >0 and pay_amount.isdigit():
        pay_amount = int(pay_amount)
        transaction_result = make_transaction(trans_logger,account_data,'repay',pay_amount)
        if  transaction_result['status'] == 0:
            print('''\033[42;1mNew Balance:%s\033[0m''' %(account_data['data']['balance']))
        else:
            print(transaction_result)

