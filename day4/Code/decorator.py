#!/usr/bin/env python
# Funtion:      
# Filename:
import time

def timeer(func):
    def warpper(*args, **kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print('the func run time is %s' %(stop_time - start_time))
    return warpper

@timeer
def foo():
    time.sleep(3)
    print('1111')

foo()
