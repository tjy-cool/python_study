#!/usr/bin/env python
# Funtion:      
# Filename:

import logging

logging.basicConfig(filename='123.log', level=logging.INFO)

# logging 的5个级别
logging.debug('test debug')
logging.info('test info')
logging.warning('test warning')
logging.error('test error')
logging.critical('test critical')