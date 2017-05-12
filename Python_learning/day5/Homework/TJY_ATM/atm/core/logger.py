#!/usr/bin/env python
# Funtion:      
# Filename:

import logging, os
from conf import settings

def logger(username, log_type):
    # 创建一个logger
    logger = logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LEVEL)

    # 设置屏幕输出的日志信息
    ch = logging.StreamHandler()
    ch.setLevel(settings.LOG_LEVEL)
    ch_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(ch_format)
    logger.addHandler(ch)

    # 设置文件输出的日志信息
    log_file = "%s/log/%s_log/%s_%s" % (settings.BASE_DIR, log_type, username, settings.LOG_TYPES[log_type])
    if os.path.exists(log_file) == False:   # 不存在该用户的日志信息，则创建新的日志文件
        f = open(log_file, 'w', encoding='utf-8')
        f.close()

    fh = logging.FileHandler(log_file, encoding='utf-8')
    fh.setLevel(settings.LOG_LEVEL)
    fh_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(fh_format)
    logger.addHandler(fh)

    return logger   # 返回logger对象

'''
    五种logger等级
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')
'''