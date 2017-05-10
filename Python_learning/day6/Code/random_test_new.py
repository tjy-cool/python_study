#!/usr/bin/env python
# Funtion:      
# Filename:

import random
import string

print(random.random())      # 生成一个随机小数
print(random.randint(1,5))      # 包含 stop
print(random.randrange(1,5))    # 不包含 stop

print(random.sample(range(100), 5))
print(random.sample("abcdef", 5))

print(string.ascii_letters)
print(string.digits)
print(string.hexdigits)

# 生成随机验证码 方式1
str_source = string.ascii_letters + string.digits
print(''.join(random.sample(str_source, 6)))

# 生成随机验证码 方式2
checkcode = ''
for i in range(6):
    current = random.randrange(0,6)
    if current != i:
        temp = chr(random.randint(65,90))       # A-Z
    else:
        temp = random.randint(0,9)
    checkcode += str(temp)
print(checkcode)
