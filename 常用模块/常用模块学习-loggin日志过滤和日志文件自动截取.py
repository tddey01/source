#!/usr/bin/env python
#_*_coding:utf-8_*_
import  logging


'''
#1生成 logger 对像
logger = logging.getLogger("web")
logger.setLevel(logging.INFO)

#生成 handler对像
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

fh = logging.FileHandler("web.log")
fh.setLevel(logging.WARNING)
#输出屏幕debug  文件warning级别


#2把handler对像 绑定到logger
logger.addHandler(ch)
logger.addHandler(fh)



#生成formatter 对像
#生成formatter 对像 绑定到 handler对像
file_formatter = logging.Formatter('%(asctime)s  -  %(name)s - %(levelname)s - %(relativeCreated)d -  %(message)s ')
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -  %(relativeCreated)d - %(message)s ')

ch.setFormatter(console_formatter)
fh.setFormatter(file_formatter)


logger.debug("test  log ")
logger.info("test log 2")
logger.error("test log 3")
logger.warning("test log 4")
logger.warn("test log 5")
'''

'''


class IgnoreBackupLogFilter(logging.Filter):
    """忽略带db backup 的日志"""
    def filter(self, record): #固定写法
        return   "db backup" not in record.getMessage()


#1生成 logger 对像
logger = logging.getLogger("web")
# logger.setLevel(logging.INFO)  #全局 优先级高
logger.setLevel(logging.DEBUG)

# 把fileter对像加载到logging 中
logger.addFilter(IgnoreBackupLogFilter())
#生成 handler对像

ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
# ch.setLevel(logging.INFO)

fh = logging.FileHandler("web.log")
# fh.setLevel(logging.WARNING)

#输出屏幕debug  文件warning级别


#2把handler对像 绑定到logger
logger.addHandler(ch)
logger.addHandler(fh)

#生成formatter 对像
#生成formatter 对像 绑定到 handler对像
file_formatter = logging.Formatter('%(asctime)s  -  %(name)s - %(levelname)s - %(relativeCreated)d -  %(message)s ')
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -  %(relativeCreated)d - %(message)s ')

ch.setFormatter(console_formatter)
fh.setFormatter(file_formatter)


logger.warning("test  log ")
logger.info("test log 2")
logger.debug("test log 3")
logger.debug(" test log db backup  3")
'''


"""
其中filename参数和backupCount参数和RotatingFileHandler具有相同的意义。

interval是时间间隔。

when参数是一个字符串。表示时间间隔的单位，不区分大小写。它有以下取值：

S 秒
M 分
H 小时
D 天
W 每星期（interval==0时代表星期一）
midnight 每天凌晨
"""

from logging import  handlers


class IgnoreBackupLogFilter(logging.Filter):
    """忽略带db backup 的日志"""
    def filter(self, record): #固定写法
        return   "db backup" not in record.getMessage()


#1生成 logger 对像
logger = logging.getLogger("web")
# logger.setLevel(logging.INFO)  #全局 优先级高
logger.setLevel(logging.DEBUG)

# 把fileter对像加载到logging 中
logger.addFilter(IgnoreBackupLogFilter())
#生成 handler对像

ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
# ch.setLevel(logging.INFO)

# fh = logging.FileHandler("web.log")
# fh.setLevel(logging.WARNING)
# fh = handlers.RotatingFileHandler("web.log",maxBytes=10,backupCount=3)
fh = handlers.TimedRotatingFileHandler("web.log",when="S",interval=5,backupCount=3)
#输出屏幕debug  文件warning级别


#2把handler对像 绑定到logger
logger.addHandler(ch)
logger.addHandler(fh)

#生成formatter 对像
#生成formatter 对像 绑定到 handler对像
file_formatter = logging.Formatter('%(asctime)s  -  %(name)s - %(levelname)s - %(relativeCreated)d -  %(message)s ')
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -  %(relativeCreated)d - %(message)s ')

ch.setFormatter(console_formatter)
fh.setFormatter(file_formatter)


logger.warning("test  log ")
logger.info("test log 2")
logger.debug("test log 3")
logger.debug(" test log db backup  3")

