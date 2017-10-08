#!/usr/bin/env python
# Funtion:      
# Filename:

from multiprocessing import Process, Lock

def fun(l, n):
    l.acquire()     # 获取锁
    print('hello world, %s' %n)
    l.release()     # 释放锁

if __name__ == '__main__':
    lock = Lock()       # 实例化锁
    for num in range(10):       # 实例化10个进程，并运行
        mul_p1 = Process(target=fun, args=(lock, num))
        mul_p1.start()
