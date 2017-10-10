#!/usr/bin/env python
# Funtion:      
# Filename:

import time, threading

def run(n, sleep_time):
    print('task: ', n, threading.current_thread())
    time.sleep(sleep_time)

start_time = time.time()

t_thread = []
for i in range(50):
    t = threading.Thread(target=run, args=('t-%s'%i ,3))
    t.start()
    t_thread.append(t)

print(threading.active_count())

for t in t_thread:
    t.join()


print('------  All Thread has finished.... -------', threading.current_thread())
print('spend time: ' , time.time() - start_time)

