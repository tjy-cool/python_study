#!/usr/bin/env python
# Funtion:      
# Filename:


# name = 'tjy'
# def foo(name):
#     print('before change: %s' % name)
#     name = "11"
#     print('after change: %s' % name)
#
# foo(name)

# import copy
# x = []
# y = copy.deepcopy(x)

# def fun(N,sum=0):
#     for i in range(0,(N-1),2):
#         sum += (i+1)*(i+2)
#         # print(i+1, i+2)
#     return sum
#
# print(fun(100))


# def print_ba(fun):
#     def wripper(*args,**kwargs):
#         print("before")
#         res = fun(*args, **kwargs)
#         print("after")
#         return res
#     return wripper
#
# @print_ba
# def f1(arg):
#     return arg + 1
# @print_ba
# def f2(arg1, arg2):
#     return arg1 + arg2
#
# print(f1(1))
# print(f2(1,2))

# 生成随机数方法一
import random
checkcode = ''
for i in range(6):
    current = random.randrange(0,6)
    if current != i:   #如果当前的loop  i不等于随机数，就取出65-90中的随机字符
        a = random.randint(0,1)
        temp = chr(random.randint(65,90)) if a == 0 else chr(random.randint(97,122))   # A-Z
    else:
        temp = random.randint(0,9)
    checkcode += str(temp)
print(checkcode)


# random.sample(str_source, 6)

# 生成随机数方法二
import random , string
str_source = string.ascii_letters + string.digits
checkcode = "".join(random.sample(str_source, 6))
print(checkcode)

# # 生成随机数方法三
# import random
# random.sample(range(10),3)