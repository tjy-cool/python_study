#!/usr/bin/env python
# Funtion:      
# Filename:
import time

# 高阶函数  把一个函数名当作实参传递给另外一个函数
#  （在不修改被装饰函数源代码的情况下为其添加功能）
def bar():
    time.sleep(0.1)
    print('in the bar')
def foo(bar):
    start_time = time.time()
    bar()
    stop_time = time.time()
    print("Sleep time: %s" % (stop_time-start_time))
    print('in the foo')
foo(bar)

# 高阶函数 返回值中包含函数名(不修改函数的调用方式)
def bar1():
    print('in the bar')
    pass
def foo1(func):
    print(func)
    return func
bar = foo1(bar1)
bar1()