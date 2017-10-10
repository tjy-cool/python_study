#!/usr/bin/env python
# Funtion:      
# Filename:

import time, threading

light_event = threading.Event()
def light():
    count = 1
    # count  0 - 5 绿灯,置1       5 - 10 红灯
    light_event.set()
    while True:
        if count<=5 :
            light_event.set()
            print('\033[42;1mgreen light on ...\033[0m')
        elif count>5 and count<=10:
            light_event.clear()
            print('\033[41;1mred light on ...\033[0m')
        else:
            count = 0
            light_event.set()
            # print('\033[41;1mred light on ...\033[0m')
        time.sleep(1)
        count += 1

def car(name):
    while True:
        if light_event.is_set():    # 绿灯
            # light_event.is_set()
            print('[%s] running ...' % name)
            time.sleep(1)
        else:   # 红灯
            print('\033[31;1m[%s] sees red light\033[0m' % name)
            light_event.wait()
            print('\033[32;1m[%s] sees green light\033[0m ' %name)


light_thread = threading.Thread(target=light)
light_thread.start()
car1 = threading.Thread(target=car, args=('Tesla',))
car1.start()
car2 = threading.Thread(target=car, args=('rose',))
car2.start()


lock = threading.Lock()     #添加一个锁的实例
lock.acquire()      # 获取一把锁
lock.release()      # 释放锁
