#!/usr/bin/env python
# Funtion:      
# Filename:

import os,sys
FILE_NAME = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(FILE_NAME))
# print(BASE_DIR)
sys.path.append(BASE_DIR)
print(sys.path)

from conf import settings
from core import main

main

main.login()
