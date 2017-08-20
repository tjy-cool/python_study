#!/usr/bin/env python
# Funtion:      
# Filename:
import os
BASE_DIR = os.path.dirname(__file__)
# print(BASE_DIR + os.sep + 'tjy')

if os.sep == "\\":
    dir = (BASE_DIR + os.sep + 'tjy').replace("/", "\\")
else :
    pass
# print("dir", dir)

if os.path.isdir(BASE_DIR):  # 判断该用户的家目录是否存在
    # print("aa")
    # print(dir)

    data = os.popen("dir %s" % dir)
    print(data.read())
