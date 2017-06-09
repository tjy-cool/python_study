#!/usr/bin/env python
# Funtion:      
# Filename:

# 斐波拉契数列， 除第一个和第二个数外，任意一个数都可以由前面两个相加得到
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        a, b = b, a+b
        # t = (b, a+b)  # t 为tuple
        # a = t[0]
        # b = t[1]
        n += 1
    # return 'done'

g = fib(6)
print(g)
while True:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:  ', e.value)
        break

# print(fib(10))
f = fib(4)
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
#
# print('======start loop=========')
# # for i in f:
# #     print(i)
# print(f.__iter__())