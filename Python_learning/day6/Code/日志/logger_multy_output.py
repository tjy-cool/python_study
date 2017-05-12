#!/usr/bin/env python
# Funtion:      
# Filename:

import logging

logger = logging.getLogger('TEST-LOG')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)
ch_format = logging.Formatter('%(asctime)s %(message)s')
ch.setFormatter(ch_format)
logger.addHandler(ch)

fh = logging.FileHandler('screen.log', encoding='utf-8')
fh.setLevel(logging.ERROR)
fh_format = logging.Formatter('%(asctime)s %(filename)s(%(lineno)d) %(message)s')
fh.setFormatter(fh_format)
logger.addHandler(fh)

logger.debug('This is a debug message')
logger.info('This is info message')
logger.warning('This is a warning message')
logger.error('This is a error message')
logger.critical('This is a critical message')
