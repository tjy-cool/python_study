#!/usr/bin/env python
# Funtion:      
# Filename:

import hashlib
'''

# md5
m = hashlib.md5()
m.update(b'hao123')
print(m.hexdigest())

m.update(b'456')
print(m.hexdigest())

m2 = hashlib.md5()
m2.update(b'hao123456')
print(m2.hexdigest())

# sha1
ha1 = hashlib.sha1()
ha1.update(b'hao1236789')
print(ha1.hexdigest())

# sha256，常用于语音消息的加密，比md5安全，使用较多
ha2 = hashlib.sha256()
ha2.update(b'hao1236789')
print(ha2.hexdigest())

ha3 = hashlib.sha384()
ha3.update(b'hao1236789')
print(ha3.hexdigest())

# ha5 = hashlib.sha512()
# ha5.update(b"hao123中国")
# print(ha5.hexdigest())


with open('a.txt','rb') as f:
    a = f.read()
    ha5 = hashlib.md5()
    ha5.update(a)
    print(ha5.hexdigest())

with open('a.txt','r',encoding='utf-8') as f:
    a = f.read()
    ha5 = hashlib.md5()
    ha5.update(bytes(a,encoding='utf-8'))
    print(ha5.hexdigest())
'''
# with open('ARA95.pdf','rb') as f:
#     a = f.read()
#     ha5 = hashlib.md5()
#     ha5.update(a)
#     print(ha5.hexdigest())
#
# with open('nsatool.exe','rb') as f:
#     a = f.read()
#     ha5 = hashlib.md5()
#     ha5.update(a)
#     print(ha5.hexdigest())

with open('nsatool.exe','rb') as f:
    a = f.read()
    sh1 = hashlib.sha1()
    sh1.update(a)
    print(sh1.hexdigest())

    ha5 = hashlib.md5()
    ha5.update(a)
    print(ha5.hexdigest())