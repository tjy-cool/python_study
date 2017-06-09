#!/usr/bin/env python
# Funtion:      
# Filename:

import logging

class aaa(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sayhi(self):
        print("Hi, my name is %s, I'm %s years old" % (self.name, self.age))
    def printid(self):
        print(id(self))

tjy = aaa('tjy',18)
tjy.sayhi()
print(id(tjy))
tjy.printid()