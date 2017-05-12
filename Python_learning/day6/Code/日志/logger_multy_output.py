#!/usr/bin/env python
# Funtion:      
# Filename:

import logging

logger = logging.getLogger('TEST-LOG')  # 创建一个logger
logger.setLevel(logging.DEBUG)      # 设置最低等级

ch = logging.StreamHandler()    # 屏幕输出
ch.setLevel(logging.WARNING)    # 设置屏幕输出的日志等级
ch_format = logging.Formatter('%(asctime)s %(message)s')    # 定义日志输出格式
ch.setFormatter(ch_format)  # 设置日志输出格式
logger.addHandler(ch)   # 将屏幕输出日志的设置增加到logger中

fh = logging.FileHandler('screen.log', encoding='utf-8')    # 定义日志输出到文件
fh.setLevel(logging.ERROR)      # 设置输出日志等级
fh_format = logging.Formatter('%(asctime)s %(filename)s(%(lineno)d) %(message)s')   # 定义日志输出格式
fh.setFormatter(fh_format)  # 设置输出格式
logger.addHandler(fh)   # 将文件输出日志的设置增加到logger中

logger.debug('This is a debug message')
logger.info('This is info message')
logger.warning('This is a warning message')
logger.error('This is a error message')
logger.critical('This is a critical message')
