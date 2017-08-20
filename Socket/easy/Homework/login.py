#!/usr/bin/env python
# Funtion:      
# Filename:

class Ftp(object):
    def __init__(self):
        pass

    @staticmethod
    def login(func):
        def wripper(*args, **kwargs):
            print("in wripper")
        return wripper

    @login
    def send_file(self):
        print("send_file")
        pass

    def recv_file(self):
        pass

aa = Ftp()
aa.login("bb")


# def login(func):
#     def wripper(*args, **kwargs):
#         func(*args, **kwargs)
#         print("in wripper")
#     return wripper
#
# @login
# def send_file():
#     print("send_file")
#     pass
#
# send_file()