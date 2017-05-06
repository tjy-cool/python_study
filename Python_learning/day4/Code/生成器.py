#!/usr/bin/env python
# Funtion:      
# Filename:

a = ( x*2 for x in range(100) )
print(a.__next__())
print(a.__next__())