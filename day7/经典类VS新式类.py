#!/usr/bin/env python
# Funtion:      
# Filename:

class A(object):
    def __init__(self):
        self.n = "A"

class B(A):
    def __init__(self):
        self.n = "B"
    # pass

class C(A):
    def __init__(self):
        self.n = "C"

class D(B,C):
    def __init__(self):
        self.n = "D"
    # pass

d = D()
print(d.n)