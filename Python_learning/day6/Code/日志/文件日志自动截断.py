#!/usr/bin/env python
# Funtion:      
# Filename:
import logging
from logging import handlers
logger = logging.getLogger('TEST')
logfile = 'timelog.log'
fh = handlers.RotatingFileHandler(filename=logfile, maxBytes=10, backupCount=3, encoding='utf-8')

formatter = logging.Formatter('%(asctime)s %(module)s:%(lineno)d %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

logger.warning('Test1')
logger.warning('Test12')
logger.warning('Test13')
logger.warning('Test14')
logger.warning('Test15')
