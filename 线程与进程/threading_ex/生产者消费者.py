#!/usr/bin/env python
# Funtion:      
# Filename:

import threading, time, queue

q = queue.Queue(maxsize=10)
def Producer(name):
    count = 1
    while True:
        q.put('包子%s' % count)
        print('\033[32;1m生产出第%s号包子\033[0m'% count)
        count += 1
        time.sleep(0.5)

def Consumer(name):
    while True:
        print('\033[31;1m%s 吃了%s\033[0m' %(name, q.get()))
        time.sleep(0.8)

p1 = threading.Thread(target=Producer, args=('',))
c1 = threading.Thread(target=Consumer, args=('alex',))
c2 = threading.Thread(target=Consumer, args=('abc',))



# p1.start()
# c1.start()
# c2.start()