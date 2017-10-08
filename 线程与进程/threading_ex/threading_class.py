#!/usr/bin/env python
# Funtion:      
# Filename:

import threading, time

class MyThread(threading.Thread):
    def __init__(self, n):
        super(MyThread,self).__init__()
        self.n = n
    def run(self):
        print('runing task ', self.n)
        time.sleep(3)

if __name__ == "__main__":
    t1 = MyThread('t1')
    t2 = MyThread('t2')
    t1.start()
    t2.start()