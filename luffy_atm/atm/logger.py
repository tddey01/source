#!/usr/bin/env python
#_*_coding:utf-8_*_


import os
import logging
from luffy_atm.conf import settings

def logger(log_type):
    #创建日志
    logger = logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LEVEL)

    #创建控制台处理程序并将级别设置为调试

    ch = logging.StreamHandler()
    ch.setLevel(settings.LOG_LEVEL)
    #创建文件处理程序并设置级别为警告

    # log_file = os.path.join(settings.LOG_PATH,settings.LOG_TYPES(log_type))
    log_file = os.path.join(settings.LOG_PATH,settings.LOG_TYPES[log_type])
    # print(log_file)
    fh = logging.FileHandler(log_file)
    fh.setLevel(settings.LOG_LEVEL)
    #创建格式化程序
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levename)s- %(message)s')

    #添加格式化的CH和FH
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    #添加CH和FH到loggerh
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger

    #应用程序代码
    # '''
    # logger.debug('debug message')
    # '''

