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
    _dict = {}
    if file_handle.read() == '':
        return -1
    else :
        for line in file_handle.readlines():
            _key = line.split(split_str)[0].strip()
            _val = line.split(split_str)[1].strip()
            _dict[_key] = _val
        return _dict

