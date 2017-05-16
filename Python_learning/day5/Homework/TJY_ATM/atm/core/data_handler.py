#!/usr/bin/env python
# Funtion:      
# Filename:

import json, time, os
from conf import settings
import re

def get_all_username():
    '''
    获得data/accouonts 文件夹下的用户名列表
    :return: 已经注册了得用户名列表，如果没有一个用户注册，则返回空列表
    '''
    userdata_path = '%s/data/accounts' % settings.BASE_DIR
    userfile_name_list = os.listdir(userdata_path)
    all_user = []
    if userfile_name_list != []:
        for userfile_name in userfile_name_list:
            all_user.append(userfile_name.split('.')[0])
    return all_user

def get_user_db(username):
    userdata_path = '%s/data/accounts' % settings.BASE_DIR
    userfile = '%s/%s.json' % (userdata_path, username)
    with open(userfile, 'r', encoding='utf-8') as f:
        user_db = json.load(f)
    return user_db

def set_user_db(username,user_db):
    userdata_path = '%s/data/accounts' % settings.BASE_DIR
    userfile = '%s/%s.json' % (userdata_path, username)
    with open(userfile, 'w', encoding='utf-8') as fp:
        json.dump(user_db, fp, indent=4)

# def isnum(str):
    # if str.startwith('-'):  # 以负号开头
    #     str = str[1:]
    #     if str.count('.') == 0 and str.isdigit():
    #         return 'negative_int'   # 负整数
    #     elif str[1:].count('.') == 1 and str.startwith('.') and str[1:].isdigit():
    #         return 'negative_non'
    #     elif
    # if re.search('^\d+$',str) != None:
    #     return 'int'
    # elif re.search('^\d+\.?\d*$',str) != None:
    #     return 'negative'
    # elif re.search('^[\+\-]?(\d*\.)?\d*$',str) == None:
    #     return False
    # else :
    #     return True


def file_data_handle(conn_params):
    print('file db:',conn_params)
    return file_execute

def data_handler():

    conn_params = settings.DATABASE
    if conn_params['engin'] == 'file_storage':
        return file_data_handle(conn_params)
    elif conn_params['engin'] == 'mysql':
        pass

def file_execute(sql, **kwargs):
    conn_params = settings.DATABASE
    db_path = '%s/%s' % (conn_params['path'], conn_params['name'])

    print(sql,db_path)
    sql_list = sql.split("where")
    print(sql_list)
    if sql_list[0].startswith("select") and len(sql_list)> 1:#has where clause
        column,val = sql_list[1].strip().split("=")

        if column == 'account':
            account_file = "%s/%s.json" % (db_path, val)
            print(account_file)
            if os.path.isfile(account_file):
                with open(account_file, 'r') as f:
                    account_data = json.load(f)
                    return account_data
            else:
                exit("\033[31;1mAccount [%s] does not exist!\033[0m" % val )

    elif sql_list[0].startswith("update") and len(sql_list)> 1:#has where clause
        column, val = sql_list[1].strip().split("=")
        if column == 'account':
            account_file = "%s/%s.json" % (db_path, val)
            #print(account_file)
            if os.path.isfile(account_file):
                account_data = kwargs.get("account_data")
                with open(account_file, 'w') as f:
                    acc_data = json.dump(account_data, f, indent=4)
                return True