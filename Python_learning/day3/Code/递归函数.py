#!/usr/bin/env python
# Funtion:      
# Filename:

def calc(n):
    print(n)
    if int(n/2) > 0 :
        return calc( int(n/2) )
    print('->',n)
calc(10)

def show_star(n):
    for i in range(n):
        print((i+1)*'*')
show_star(10)

