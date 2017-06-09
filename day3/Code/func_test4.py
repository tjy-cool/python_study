#!/usr/bin/env python
# Funtion:      
# Filename:

def fun2():
    '''fun2'''
    print('in the fun2')

def fun1():
    '''fun1'''
    print('in the fun1')
    # return 1, '34a', [123,34],{'name':'tjy'},set(['3445','dfds'])
    return fun2

a = fun1()
print(a)

