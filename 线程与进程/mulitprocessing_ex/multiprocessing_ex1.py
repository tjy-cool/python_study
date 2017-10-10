#!/usr/bin/env python
# Funtion:      
# Filename:

import multiprocessing, time
import threading

def threading_run(num):
    print('multiprocess [%s], threading id: %s'%(num,threading.get_ident()))

def multiprocess_run(name, num):
    print('%s running...' % name )
    t1 = threading.Thread(target=threading_run, args=(num,))
    t1.start()
    print('--------',t1.getName(),t1.ident, threading.get_ident())
    # print()
    time.sleep(2)

if __name__ == '__main__':
    for i in range(10):
        # 创建进程
        p = multiprocessing.Process(target=multiprocess_run, args=('bob_%s' % i,i))
        p.start()

