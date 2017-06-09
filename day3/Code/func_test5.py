#!/usr/bin/env python
# Funtion:      
# Filename:
# 参数的类型
# 1. 形参和实参
# 2. 位置参数和关键字
# 3. 默认参数
# 4. 参数组

# # 2. 位置参数和关键字
# def fun1(x,y):
#     print(x)
#     print(y)
# # fun1(1, 2)        # 位置参数
# # fun1(x=1, y=2)    # 关键参数
# # fun1(y=2, x=1)
# # fun1(y=1, 3)      # 出错,关键字参数不能出现在位置参数之前
# fun1(1, y=3)        # 正确

# 3. 默认参数
# 特点：调用默认参数可以不写
# 用途：


# def fun2(x, list=[]):
#     list.append(x)
#     return list
# # 方式一
# print(fun2(10))
# print(fun2(1))
# print(fun2('x'))

# def fun2(x, list=[]):
#     list.append(x)
#     return list
# # 方式二
# print(fun2(10))
# print(fun2(1, []))
# print(fun2('x'))

# def fun2(x, list=[]):
#     list.append(x)
#     return list
# # 方式三
# list1 = fun2(10)
# list2 = fun2(1, [])
# list3 = fun2('x')
# print(list1)
# print(list2)
# print(list3)

# def fun2(x, list=[]):
#     list.append(x)
#     return list
# # 方式四
# # list1 = fun2(10)
# # print(list1)
# # list2 = fun2(1)
# # list3 = fun2('x')
# list1 = fun2
# list2 = fun2
# list3 = fun2
# list4 = fun2(10)
# print(list1)
# print(list2)
# print(list3)
# print(list4)
#
# def fun3():
#     print('Hello')
#     return 3
# # print(fun3)
# # print(fun3)
# # print(fun3)
#
# tuple1 = (1,2,3,4)
# print(tuple1)
# print(tuple1[1])

name = '123'
print(name)
while True:
    if 1<2:
        name = '234'
        print(name)
        break
print(name)


