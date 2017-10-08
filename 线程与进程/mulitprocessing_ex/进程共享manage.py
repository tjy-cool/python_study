#!/usr/bin/env python
# Funtion:      
# Filename:

from multiprocessing import Process, Manager
import os

def fun(d, l):
    # os.getpid()为获取进程的id号，而os.getppid()为获取进程的父PID号
    d[os.getpid()] = os.getpid()
    l.append(os.getpid())

if __name__ == "__main__":
    with Manager() as manage:
        d = manage.dict()       # 生成一个字典，可以在多个进程之间共享数据
        l = manage.list(range(5))
        p_list = []
        for i in range(10):
            mul_p1 = Process(target=fun, args=(d,l))
            mul_p1.start()
            p_list.append(mul_p1)

        for res in p_list:      # 必须要等待进程运行完，否则运行出错
            res.join()
        print(d)
        print(l)