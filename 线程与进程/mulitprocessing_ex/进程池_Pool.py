#!/usr/bin/env python
# Funtion:      
# Filename:

from multiprocessing import  Process, Pool
import time,os

def Foo(i):
    time.sleep(2)
    print('in process', os.getpid())
    return i+100

def Bar(args):
    print('--->exec done:', args, os.getpid())

if __name__ == '__main__':
    pool = Pool(processes=10)
    print('主进程', os.getpid())
    for i in range(10):
        # pool.apply(func=Foo, args=(i,))
        # pool.apply_async(func=Foo, args=(i,))
        pool.apply_async(func=Foo, args=(i,), callback=Bar)

    print('end')
    pool.close()
    pool.join()