#!/usr/bin/env python
# Funtion:      
# Filename:
def add(a, b, f):
    return f(a) + f(b)

res = add(3, -6, abs)
print(res)


def fun(x):
    return x**3
def fun1(x, y, fun):
    return fun(x)+fun(y)
a = fun1(1, 3, fun)
print(a)