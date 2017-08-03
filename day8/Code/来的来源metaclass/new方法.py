#!/usr/bin/env python
# Funtion:      
# Filename:

class Foo(object):
    def __init__(self, name):
        self.name = name

        print("Foo __init__")
    
    def __new__(cls, *args, **kwargs):
        print("Foo __new__", cls, *args, **kwargs)
        print(object.__new__(cls))
        return object.__new__(cls)
    
f = Foo("tjy")

        