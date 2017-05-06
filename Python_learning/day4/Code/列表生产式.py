#!/usr/bin/env python
# Funtion:      
# Filename:

# 方式一
list = []
for i in range(10):
    list.append(i**2)
print(list)

# 方式二， 列表生成式
print([ x**2 for x in range(10) ])

# 方式三
def func(x):
    return x**2
a = [func(i) for i in range(10)]
print(a)

