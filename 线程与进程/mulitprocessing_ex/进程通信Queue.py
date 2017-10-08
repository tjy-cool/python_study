#!/usr/bin/env python
# Funtion:      
# Filename:

from multiprocessing import Process, Queue

def fun(data, qq):
    qq.put('In subprocessing, %s' % data)

if __name__ == '__main__':
    q = Queue()
    mul_p = Process(target=fun, args=([12, 'fsa', {1:'liming', 2:'lixiang'}],q))
    mul_p.start()
    print(q.get())
    mul_p.join()