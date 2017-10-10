#!/usr/bin/env python
# Funtion:      
# Filename:

# os.system(cd ../)     # 不可用
# os.chdir()            # 不好使，
# 最好使用字符串， /home/tjy/python/code
# cd python, 将字符串改为 /home/tjy/python/code/python
# cd .., 将字符串改为 /home/tjy/python/code

import socketserver, os, hashlib, json

ALL_CMD = ['ls', 'push', 'pull', 'cd', 'ifconfig', 'df']

class MyTCPHandle(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print(self.data)
                cmd_dic = json.loads(self.data.decode())
                action = cmd_dic['action']
                if hasattr(self, 'cmd_%s'%action):
                    func = getattr(self, 'cmd_%s'%action)
                    func(cmd_dic)



            #     cmd = self.data.split(' ')[0]
            #     if cmd in ALL_CMD:
            #         if hasattr(self, 'cmd_'+cmd):
            #             fun = getattr(self, 'cmd_'+cmd)
            #             fun(self.data)
            #         else :
            #             self.cmd_defalut(self.data)
            except ConnectionResetError as e:
                print('error: ', e)
                break

    def cmd_push(self, *args):
        '''接收客户端文件'''
        cmd_dic = args[0]
        file_name = cmd_dic['filename']
        file_size = cmd_dic['size']
        if os.path.isfile(file_name):
            f = open(file_name + 'new', 'wb')
        else:
            f = open(file_name, 'wb')
        self.request.send('200 ok'.encode())     # 应该返回json格式
        recv_size = 0
        while recv_size < file_size:
            if file_size - recv_size >1024:
                size = 1024
            else :
                size = file_size-recv_size
            data = self.request.recv(1024)
            recv_size += len(data)
        else:
            print('file [%s] has pushed done...' %file_name)

        pass

    def cmd_pull(self, *args):
        pass
    def cmd_defalut(self, *args):
        pass

if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 9999
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandle)
    server.serve_forever()
    server.server_close()