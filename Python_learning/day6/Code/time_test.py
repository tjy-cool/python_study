#!/usr/bin/env python
# Funtion:      
# Filename:

import time
import datetime

print(time.clock())     # 返回处理器时间，3.3库已经开始废弃，改成了time.process_time()测量处理器运算时间，不包括sleep时间，mac上测不出来
print(time.process_time())
print(time.altzone) # 返回与UTC时间的时间差，以秒计算
print(time.asctime())   # 返回时间格式：Wed May 10 16:34:40 2017

t = time.localtime( time.time() + 3600*3 )       # 本地时间
print(t, t.tm_year, t.tm_yday)     # tm_yday表示year to day，既今年的第几天
print(time.localtime()) # 返回本地时间的 struct time对象格式

print(time.time())  # 时间戳，从1970年1月1日开始算起的多少秒
print(time.gmtime())    # utc time

print(time.asctime(t))
print(time.ctime())

t2 = time.strptime('2016-11-11 23:30', '%Y-%m-%d %H:%M')    # 时间对象
t2_stamp = time.mktime(t2)    # 时间戳
print(time.mktime(t2))

t3 = time.localtime(t2_stamp)   # 时间对象
t3_str = time.strftime('%Y_%m_%d_%H_%M')
print(t3,t3_str)

print("datetime".center(60, "-"))
print(datetime.datetime.now())
print(datetime.datetime.fromtimestamp(time.time() - 3600))

now = datetime.datetime.now()

print(now.replace(year=2016,month = 2))
