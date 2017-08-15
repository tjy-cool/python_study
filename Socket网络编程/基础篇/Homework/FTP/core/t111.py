#!/usr/bin/env python
# Funtion:      
# Filename:

def add_print_hello(func):
    def wripper(*args, **kwargs):
        print(args)
        print("hello")
        func(*args, **kwargs)
    return wripper

class school(object):
    # def __init__(self, ip, port):
    #     self.ip = ip
    #     self.port = port

    @add_print_hello
    def connect(self, data):
        print('aaa', data)



shl = school()
shl.connect("1234")