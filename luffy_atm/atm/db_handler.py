#!/usr/bin/env python
#_*_coding:utf-8_*_


import time, json
import os,sys

from luffy_atm.conf import settings


def load_account_data(account):
    '''根据account id 找到对应的账户文件 并加载文件里面的数据'''
    account_file = os.path.join(settings.DB_PATH,"%s.json" % account)
    if os.path.isfile(account_file):
        f = open(account_file)
        data = json.load(f)
        f.close()
        return {'status':0,'data':data}
    else:
        return  {'status':-1,'error':"account file  does not exist"}


def save_db(account_data):
    '''根据account_data找到对应的账户文件，把内存里面的数据保存到硬盘里面'''
    account_file  = os.path.join(settings.DB_PATH,"%s.json"% account_data['%d'])
    if  os.path.isfile(account_file):
        f = open("%s.new" % account_file,'w')
        data = json.dump(account_data,f)
        f.close()
        os.rename("%s.new" % account_file,account_file)
        return  {"status":0,'data':data}
    else:
        return  {'status':-1 , 'error':'acconut file does not exits'}

