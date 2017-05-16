#!/usr/bin/env python
# Funtion:      
# Filename:

import time

def count_time(fun):
    def wripper(*args, **kwargs):
        start_time = time.time()
        print(args[0])
        fun(*args, **kwargs)
        stop_time = time.time()
        print(stop_time-start_time)
    return wripper

@count_time
def calc(n):
    for i in range(n):
        time.sleep(0.1)

calc(5)