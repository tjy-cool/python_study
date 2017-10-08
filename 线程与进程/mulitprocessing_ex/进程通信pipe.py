#!/usr/bin/env python
# Funtion:      
# Filename:

from multiprocessing import Process, Pipe

def fun(conn):
    conn.send('from child, 0')
    conn.send('from child, 1')
    print(conn.recv())

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    mul_p1 = Process(target=fun, args=(child_conn, ))
    mul_p1.start()

    parent_conn.send('from parent, hahahaha')
    print(parent_conn.recv())
    print(parent_conn.recv())
