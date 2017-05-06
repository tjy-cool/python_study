#!/usr/bin/env python
# Filename: file_test.py

f = open('水手-歌词.1.txt','r',encoding='utf-8')    # 文件句柄
# a = f.readlines()
f.seek(20)
# f.write('tjy')
# print(f.tell())

# print(f)
# print(a.encode())
# print(f.tell())
# f.seek(0)
# f.write('1234abc')
f.truncate(5)
# f1 = f.read()
# f2 = f.read()
# print(f1)
# f.write('second'.center(50,'='))

# print()
# print(f2)

with open('a.txt', 'a+') as f1:
    # f1.write(b'end action')
    f1.seek(0)
    print(f1.tell())
    str1 = f1.write('nhao')
    print(f1.tell())
print(str1)
