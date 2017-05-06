#!/usr/bin/env python
# Funtion:      
# Filename:

def input_2_dict(cnt = 8):
    '''
    将输入的字典格式的字符串 转换为 程序中的字典
    输入格式如下：
    """
    {
        'bakend': 'www.oldboy.org',
        'record':{
            'server': '100.1.7.9',
            'weight': 20,
            'maxconn': 30
        }
    }
    """
    :param cnt: 字符串格式的字典的有效行数
    :return:    转换后的字典
    '''
    input('Please input a dict of backend and server:')
    str = ''
    for i in range(cnt):
        str += input().strip()
    str2dict = eval(str)
    return str2dict

print(len(input_2_dict(5)))