#!/usr/bin/env python
# Funtion:      
# Filename:

# print(all([1,2,0]))     # 有0为False，其余为True， 空为True
# print(any([1,0,1]))     # 全部是0为False, 空位False, 其余为True
#
# a = ascii([123,23])     # 转换为字符串格式
# print(type(a))
#
# print(bin(123))         #   转换为二进制数，'0b1111011'

# print( bool( [0] ) )   # 0、空、空列表、空字典 统统为False，其余为True

# a = bytes('abcd', encoding='utf-8')
# print(a.capitalize(), a)    # b'Abcd' b'abcd'

# b = bytearray('abcd', encoding='utf-8')
# print(b[1])   # 98
# # b[1] = 'd'    # 错误
# b[1] = 100
# print(b)

# print(callable( [] ))   # 判断是否可以被调用，理解为可以加 ()

# print( chr(100) )       # 把数字转换为ascii码的字母
# print( ord('c') )       # 把ascii码的字母转换为数字

# code = 'for i in range(10):print(i) '
# c = compile(code, '', 'exec')       # <code object <module> at 0x00C229D0, file "", line 1>
# exec(c)
#
# code1 = '100+3/2*6'
# c1 = compile(code1, '', 'eval')       # <code object <module> at 0x00C229D0, file "", line 1>
# print(eval(c1))

# dir({})     # 所有方法

# print(divmod(1,3))   # 返回商和余数

# 匿名函数 lambda
# def sayhi(n):
#     print(n**3)
# sayhi(3)
# # (lambda n: print(n**3)) (5)
# calc = lambda n : print(n**3)
# calc(3)

# res = filter(lambda n : n>5, range(10))       # 过滤得到 大于5的数据
# res = filter(lambda n : n%2==1, range(10))    # 过滤得到 奇数
# res = filter(lambda n : n%2==0, range(10))    # 过滤得到 偶数
# res = filter(lambda n: n != 0, range(10))     # 过滤得到 非零数据
# res  = map(lambda n: n*2, range(10))            # [i*2 for i in range(10)]
# # res = [lambda i:i*2 for i in range(10)]
# for i in res:
#     print(i)

# import functools
# # res = functools.reduce(lambda x,y: x+y,range(10))   # 求和
# res = functools.reduce(lambda x,y: x*y,range(1,10))   # 求阶乘
# print(res)

# a = set([1,3,4,3,445,45,34,34])
# a = frozenset([1,3,4,3,445,45,34,34])   # 冻结集合，可以有重复
# print(a)

# print(globals())    # 本文件所有的key-value变量
# def test():
#     local_var = 333
#     print(local_var)
#     print(locals())
# test()
# print(globals().get('local_var'))


# hash('hello')       # 返回hash算法计算后的结果

# print(hex(255))   # hex 为16进制
# print(oct(9))       # oct 为八进制

# print(pow(2,8))
#
# repr(object)

# print(reversed([1,2,3,44]))

# slice(2,5)  # 忘记吧

# a = {6:2, 8:0, 1:4, -5:6, 99:11, 4:22}

# print(sorted(a.items()))    # 按key排序
# print(sorted(a.items(), key = lambda x:x[1]))    # 按value排序

# a = [1,2,3,4,5,6]
# b = ['a', 'b', 'c', 'd']
# for i in zip(a,b):      # map
#     print(i)

# import decorator
__import__('decorator')
