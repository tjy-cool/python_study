#!/usr/bin/env python
# Funtion:      
# Filename:

import threading, os, time

lock = threading.Lock()

def run(n):
    lock.acquire()
    global num
    num += 1
    # time.sleep(0.1)
    lock.release()

num = 0
threading_obj = []
for i in range(1000):
    t = threading.Thread(target=run, args=('t1',))
    # t.setDaemon(True)
    t.start()
    threading_obj.append(t)

for t in threading_obj:
    t.join()

print("---------- main threading running done....-------", threading.current_thread())
print('num:',num)