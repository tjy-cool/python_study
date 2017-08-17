# #!/usr/bin/env python
# # Funtion:
# # Filename:
#
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

    def con(self):
        self.connect(123)



shl = school()
shl.con()
# shl.connect("1234")


# import os
# print(os.popen('dir').read())

# def decorator(args):
#     def _deco(func):
#         def _func(self):
#             # 注意 self 是作为参数传进来的
#             self.i = args
#             func(self)
#         return _func
#     return _deco
#
# class Foo(object):
#     @decorator(123)
#     def bar(self):
#         # 输出 123
#         print('i:', self.i)
#
#
#
# f = Foo()
# f.bar()
