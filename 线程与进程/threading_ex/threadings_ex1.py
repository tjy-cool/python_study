#!/usr/bin/env python
# Funtion:      
# Filename:

import threading
import time

def run(n):
    print("task", n)
    time.sleep(2)

t1 = threading.Thread(target=run, args=('t1',))
t1.start()
t2 = threading.Thread(target=run, args=('11111',))
t2.start()

print('--------')
run('t1')
run('23')