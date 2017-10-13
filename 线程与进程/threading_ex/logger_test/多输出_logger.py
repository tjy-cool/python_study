#!/usr/bin/env python
# Funtion:      
# Filename:

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)
ch_fmt = logging.Formatter('%(asctime)s %(lineno)d  %(message)s ')
ch.setFormatter(ch_fmt)
logger.addHandler(ch)

fh = logging.FileHandler('screen.log', encoding='utf-8')
fh.setLevel(logging.ERROR)
fh_fmt = logging.Formatter('%(asctime)s %(filename)s：%(lineno)d %(message)s ')
fh.setFormatter(fh_fmt)
logger.addHandler(fh)

logger.debug('debug test')
logger.info('This is info message')
logger.warning('This is a warning message')
logger.error('This is a error message')
logger.critical('This is a critical message')
