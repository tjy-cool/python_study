#!/usr/bin/env python
# Funtion:      
# Filename:

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HOST, PORT = 'localhost', 9999

USER_DATA = {
    'user_name': None,
    'passwd_md5': None,

    # -1表示没有任何人登陆， 0表示本次登陆成功，1表示已经在其他设备登陆中
    'is_authenticated': -1,
    'locked': 0     # 0表示已经未锁住了，1表示锁住了，输错了三次密码就会锁住
}

# 自定义错误类型
MYERRORS = {
    0: "Success",           # 成功
    1: "Unknown error",     # 未知错误
    2: "Invalid user id",    # 无效的user id
    3: "Username has been locked"   # 用户名已经锁住了

}

# log等级设置


