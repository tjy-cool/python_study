#!/usr/bin/env python
# Funtion:      
# Filename:

import os,sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from example import example
from core import main
if __name__ == '__main__':
    # pass
    example.logger_test()  # 测试日志程序
    # example.login_test()
    print('New:Balance: \033[32;1m%s\033[0m' % '234')
    # print("you have been revoke your account at the time： "
    #       "\033[1;32m %s\033[0m " % '234')
    # main.run()
#     menu_title = ("\033[32;m %s's Bank \033[0m" % 'fsdfsfsa').center(55, '-')
#     menu_body = '''\033[31;1m
#     1. 账户信息      2. 还款       3. 取款
#     4. 转账          5. 账单       6. 退出\033[0m
# '''
#     menu = menu_title + menu_body + '-' * 44
#     print(menu)