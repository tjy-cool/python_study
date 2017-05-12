#!/usr/bin/env python
# Funtion:      
# Filename:

from core import logger
def logger_test():
    '''
    测试core/logger.py的程序
    :return: 
    '''
    # 提款，还款，转账，查余额，查账单 信息日志
    access_logger = logger.logger('0001','access')
    transaction_logger = logger.logger('0001','transaction')
    # 交易信息日志
    access_logger.info('This is a access logger')
    transaction_logger.info('This is a transaction logger')

from core import login
def login_test():

    login.acc_login('userdata')
    # login.islocked('0001')
