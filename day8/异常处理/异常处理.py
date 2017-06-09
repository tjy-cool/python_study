#!/usr/bin/env python
# Funtion:      
# Filename:

# 简单情况
name = [123,234]
try :
    name[3]
except IndexError as e:
    print('简单情况错误',e)

# 同时处理两种错误
data = {}
try:
    print(name[3])  # 运行到此处出错
    print(data['name'])
except KeyError as e:
    print('同时处理两种错误', e)
except IndexError as e2:
    print('同时处理两种错误', e2)

# 或者
try:
    print(name[3])     # 运行到此处出错
    print(data['name'])
except (KeyError,IndexError) as e:
    print('或者',e)

# 再者
try:
    print(name[3])  # 运行到此处出错
    print(data['name'])
except Exception as e:  # 抓住所有的错误，一般不用
    print('再者',e)

# 文件情况
try:
    open('aa.txt')   # FileNotFoundError
except FileNotFoundError as e:
    print(e)