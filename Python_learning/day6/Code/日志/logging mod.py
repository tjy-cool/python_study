#!/usr/bin/env python
# Funtion:      
# Filename:

import logging
# logging.basicConfig(filename='app.log', level=logging.WARNING)
logging.basicConfig(filename='app.log',
                    level=logging.WARNING,
                    format='%(asctime)s %(filename)s (%(lineno)d) - %(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

logging.debug("debug")
logging.info('info')
logging.warning("warning")
logging.error('error')
logging.critical("critical")

logging.basicConfig(filename='app.log',
                    level=logging.WARNING,
                    format='%(asctime)s %(filename)s %(funcName)s (%(lineno)d) - %(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
def app_run():
    logging.warning('app has been run too long ...')
app_run()