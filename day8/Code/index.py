#!/usr/bin/env python
# Funtion:      
# Filename:



from lib.aa import  C

obj = C('haha')

print(obj.__module__)   # 输出lib.aa，即：输出模块
print(obj.__class__)    # 输出lib.aa.C, 即输出类名