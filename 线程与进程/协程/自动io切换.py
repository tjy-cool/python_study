#!/usr/bin/env python
# Funtion:      
# Filename:

import gevent

def foo():
    print('Foo running')
    gevent.sleep(3)
    print('Explicit context switch to foo again')
def bar():
    print('Explicit context to bar')
    gevent.sleep(1)
    print('Imlicit context switch back to bar')

def func():
    print('func running')
    gevent.sleep(0)
    print('func running again')

gevent.joinall([
gevent.spawn(foo),
    gevent.spawn(bar),
    gevent.spawn(func),
])