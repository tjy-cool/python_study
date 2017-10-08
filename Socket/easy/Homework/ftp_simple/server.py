#!/usr/bin/env python
# Funtion:      
# Filename:

import socketserver, os, hashlib

ALL_CMD = ['ls', 'push', 'pull', 'cd', 'ifconfig', 'df']

class MyTCPHandle(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).decode()
                cmd = self.data.split(' ')[0]
                if cmd in ALL_CMD:
                    if hasattr(self, 'cmd_'+cmd):
                        fun = getattr(self, 'cmd_'+cmd)
                        fun(self.data)
                    else :
                        self.cmd_defalut(self.data)
            except ConnectionResetError as e:
                print('error: ', e)
                break

    def cmd_push(self, *args):

        pass

    def cmd_pull(self, *args):
        pass
    def cmd_defalut(self, *args):
        pass

if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 22
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandle)
    server.serve_forever()
    server.server_close()