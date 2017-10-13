#!/usr/bin/env python
# Funtion:      
# Filename:

# def fun():
#     print('123')
# Fun = fun
#
# print('id:Fun---', id(Fun))
# print('id:fun---', id(fun))

import threading, time
import logging

class MyThread(threading.Thread):
    def __init__(self, n):
        super(MyThread,self).__init__()
        self.n = n

    def Run(self):
        print('ident', threading.get_ident())
        print('runing task ', self.n)
        self.name = '123-thread'
        print('name',self.name)
        time.sleep(3)
    run = Run

if __name__ == "__main__":
    t1 = MyThread('t1')
    t2 = MyThread('t2')
    t1.start()
    t2.start()