#!/usr/bin/env python
# Funtion:      
# Filename:

import time, threading

def runing(n, sleep_time):
    print('task: ', n, threading.current_thread())
    time.sleep(sleep_time)

start_time = time.time()

t_thread = []
for i in range(50):
    t = threading.Thread(target=runing, args=('t-%s'%i ,3))
    t.setDaemon(True)       # 设置为守护线程
    t.start()
    t_thread.append(t)

# for t in t_thread:
#     t.join()          # 等待各子线程结束

print(threading.active_count())
print('------  All Thread has finished.... -------', threading.current_thread())
print('spend time: ' , time.time() - start_time)

