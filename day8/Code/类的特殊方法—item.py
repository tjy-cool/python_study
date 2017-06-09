#!/usr/bin/env python
# Funtion:      
# Filename:

# __getitem__(self, item)
# __setitem__(self, key, value)
# __delitem__(self, key)

class Foo(object):
    def __init__(self):
        self.data = {}

    def __getitem__(self, item):
        print('__getitem__', item)
        return self.data.get(item)

    def __setitem__(self, key, value):
        print('__setitem__', key, value)
        self.data[key] = value

    def __delitem__(self, key):
        print('__delitem__', key)


F = Foo()
F['name'] = 'haha'
# print(F['name'])
# print(F.data)

del F['123']