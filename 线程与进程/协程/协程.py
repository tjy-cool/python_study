#!/usr/bin/env python
# Funtion:      
# Filename:
import time
# from greenlet import greenlet

def home():
    print('in func 1')
    time.sleep(5)       # 此时的5秒钟相当于从数据库中取数据的时间
    print('home exec done...')

def bbs():
    print('in func 2')
    time.sleep(2)

def login():
    print('in func 3')



