#!/usr/bin/env python
# Funtion:      
# Filename:

import os,sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from example import example

if __name__ == '__main__':
    # pass
    # example.logger_test()  # 测试日志程序
    example.login_test()
    # print("you have been revoke your account at the time： "
    #       "\033[1;32m %s\033[0m " % '234')
