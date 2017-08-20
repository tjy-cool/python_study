# # #!/usr/bin/env python
# # # Funtion:
# # # Filename:
# #
# def add_print_hello(func):
#     def wripper(*args, **kwargs):
#         print(args)
#         print("hello")
#         func(*args, **kwargs)
#     return wripper
#
# class school(object):
#     # def __init__(self, ip, port):
#     #     self.ip = ip
#     #     self.port = port
#
#     @add_print_hello
#     def connect(self, data):
#         print('aaa', data)
#
#     def con(self):
#         self.connect(123)
#
#
#
# shl = school()
# shl.con()
# # shl.connect("1234")
#
#
# # import os
# # print(os.popen('dir').read())
#
# # def decorator(args):
# #     def _deco(func):
# #         def _func(self):
# #             # 注意 self 是作为参数传进来的
# #             self.i = args
# #             func(self)
# #         return _func
# #     return _deco
# #
# # class Foo(object):
# #     @decorator(123)
# #     def bar(self):
# #         # 输出 123
# #         print('i:', self.i)
# #
# #
# #
# # f = Foo()
# # f.bar()




from wsgiref.simple_server import make_server

def RunServer(environ, start_response):
    start_response("200 OK", [('Content-Type', 'text/html')])
    return '<h1>Hello, web!</h1>'

if __name__ == "__main__":
    httpd = make_server("", 8000, RunServer)
    print("Serving HTTP on port 8000...")
    # while循环，等到用户请求到来
    # 只要有请求进来，执行RunServer函数
    httpd.serve_forever()