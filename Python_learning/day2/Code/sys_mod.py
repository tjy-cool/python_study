#!/usr/bin/env python
# Author:tjy


import sys
print(sys.path)
print(sys.argv)     #打印相当路径
print(sys.argv[1])


'''
import os

dir_res = os.system("dir")
print("--->", dir_res)

dir_res = os.popen("dir").read()
print(dir_res)
#os.mkdir("new")
print(os.getpid())
'''