#!/usr/bin/env python
# Funtion:      
# Filename:

# 信号量
import threading
# 实例化信号量锁，最大允许5个线程运行
semaphore = threading.BoundedSemaphore(5)
semaphore.acquire()     # 增加信号量锁
semaphore.release()     # 释放信号量锁


import threading, time

def run(n):
    semaphore.acquire()
    time.sleep(1)
    print('run the thread: %s\n' %n)
    semaphore.release()

if __name__ == '__main__':
    semaphore = threading.BoundedSemaphore(5)       # 信号量，最多有5个线程同时运行
    for i in range(25):
        t = threading.Thread(target=run, args=(i,))
        t.start()

while threading.active_count() != 1:
    pass
else:
    print('------all threads done ----')