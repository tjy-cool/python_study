#!/usr/bin/env python
# Funtion:      
# Filename:
#########################################################################################
'''
购物车程序：
1、启动程序后，输入用户名密码后，如果是第一次登录，让用户输入工资，然后打印商品列表
2、允许用户根据商品编号购买商品
3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
4、可随时退出，退出时，打印已购买商品和余额
5、在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示
6、用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买
7、允许查询之前的消费记录
'''
#########################################################################################

import time, sys

def welcome():
    '''登陆欢迎信息'''
    for i in range(6) :
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.2)
    print("\nwelcome! you are login...")  # 相等打印欢迎信息

def file_2_dict(file_handle, split_str):
    '''
    文件转换为字典，
    :param file_handle: 文件句柄
    :param dict: 字典
    :param split_str: 
    :return: 
    '''
    _dict = {}
    if file_handle.read() == '':
        return -1
    else :
        for line in file_handle.readlines():
            _key = line.split(split_str)[0].strip()
            _val = line.split(split_str)[1].strip()
            _dict[_key] = _val
        print(_dict)
        return _dict


# 用户登陆
# def login_fun(file_handle1, file_handle2):         #正确登陆返回1
#     file_2_dict(file_handle1)


username_passwd = {}     # 用户名密码
err_info = {}            # 错误登陆
user_file = open('username_passwd.txt', 'r+', encoding='utf-8')
print(user_file.read())
err_file = open('err.txt', 'r+', encoding='utf-8')
username_passwd = file_2_dict(user_file, ',')
print(username_passwd)
# file_2_dict(err_file, ':')