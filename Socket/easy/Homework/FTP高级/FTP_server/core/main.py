#!/usr/bin/env python
# Funtion:      
# Filename:


import socketserver
import json, hashlib, os
from conf import settings

class MyTCPHandlers(socketserver.BaseRequestHandler):
    def handle(self):
        self.authentication()  # 用户认证
        while True:
            try:
                self.data = self.request.recv(1024)
                pass
            except ConnectionResetError as e:
                print('error:', e)
                break

    def authentication(self):   # 用户登陆函数
        self.user_data = self.request.recv(1024)
        if self.user_data == b'':    # 表明已经断开了连接
            print('123')
        print(self.user_data)
        User_data = self.user_data.decode()
        username = User_data['user_name']
        user_info_dir = settings.BASE_DIR+'/db'+'/user_info'



def run():
    print("server is running...")
    server = socketserver.ThreadingTCPServer((settings.HOST, settings.PORT), MyTCPHandlers)
    server.serve_forever()
    server.server_close()