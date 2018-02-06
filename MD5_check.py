#!/usr/bin/env python
# Funtion:      
# Filename:

import hashlib
md5 = hashlib.md5()
a = '你好'
md5.update(a.encode('gb2312'))
print(md5.hexdigest())