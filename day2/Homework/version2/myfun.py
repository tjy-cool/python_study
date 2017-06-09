#!/usr/bin/env python
# Funtion:      
# Filename:
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
    dict_1 = {}
    file_handle.seek(0)
    for line in file_handle.readlines():
        key_1 = line.split(split_str)[0].strip()
        val_1 = line.split(split_str)[1].strip()
        dict_1[key_1] = val_1
    return dict_1