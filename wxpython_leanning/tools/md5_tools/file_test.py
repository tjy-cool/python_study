#!/usr/bin/env python
# Funtion:      
# Filename:

import binascii
import zlib
with open(r'E:\vscode_pragram\mine\Python3\Python_learning\wxpython_leanning\tools\md5_tools\MD5_Hash.py', 'rb') as f:
    # print(f.read())
    # print(binascii.crc32(f.read()))
    z = 0
    for i in f:
        z=zlib.crc32(i)
    print('%X'% z)

# 5290D266C4