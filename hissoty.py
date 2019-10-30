#!/usr/bin/env  python3
# coding utf-8
# import  pymysql,os,datetime,time
#
# date = datetime.datetime.now() + datetime.timedelta(days=30)
# start = time.mktime(date.timetuple())
# print(start)
# db = pymysql.connect(host = '127.0.0.1', user = 'zabbix', passwd = 'zabbix', db = 'zabbix', port = 3306 )
#
# cursor = db.cursor()
# cursor.execute('delete from history_uint where check < start')
# data  = cursor.fetchall()
# print(data)
# cursor.close()
# db.close()

import datetime

now = datetime.datetime.now().strftime("%Y-%m-%d %X")
print(now)