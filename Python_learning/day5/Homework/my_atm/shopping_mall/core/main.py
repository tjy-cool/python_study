#!/usr/bin/env python
# Funtion:      
# Filename:

from core import login
from core import data_handler
import os
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run():
    user_file = "%s/db/user_db/username_passwd.txt" % base_dir
    err_file = '%s/db/user_db/err.txt' % base_dir

    user = login.login(user_file, err_file)
    if user != '':  # 成功登陆
        shopping( 'goods_list.txt')
    else:  # 没有成功登陆
        print('login err!')

def choose_goods(goods_list):
    bought_goods_list = []
    show_goods_flag = 1
    exit_flag = False
    while not exit_flag:
        pass
    return bought_goods_list

def pay_for(goods_list):
    pass

def shopping(goods_list_file):
    with open(goods_list_file, 'r', encoding='utf_8') as f:
        goods_list = data_handler.file_2_list(f)    # 读取超市商品列表
    bought_goods_list = choose_goods(goods_list)    # 将商品加入购物车
    pay_for(bought_goods_list)  # 为选购商品付款
