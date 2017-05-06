#!/usr/bin/env python
# file_name: os_test.py

import os

# os.system("dir")    # 列出当前文件夹下的文件名称


# dir_req = os.system("dir")
# print("--->", dir_req)

dir_req = os.popen("dir")
print(dir_req)
print("\n")
print(dir_req.read())