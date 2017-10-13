#!/usr/bin/env python
# Funtion:      
# Filename:

import socket, os, hashlib, json

ALL_CMD = ['ls', 'pwd','push', 'pull', 'cd', 'ifconfig', 'df']

class FTP_Client(object):
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT
        self.client = socket.socket()
        self.client.connect((self.HOST, self.PORT))

    def run(self):
        while True:
            input_cmd = input('>>: ')       # 输入指令， 如 push aa.txt bb.txt
            if len(input_cmd) == 0:
                continue
            else:
                cmd_str = input_cmd.split(' ')[0]
                param = input_cmd.split(' ')[1:-1]
                if cmd_str in ALL_CMD:
                    # self.client.send(input_cmd.encode('utf-8'))
                    if hasattr(self, 'cmd_%s'%cmd_str):
                        obj = getattr(self, 'cmd_%s'%cmd_str)
                        obj(input_cmd)
                    else :
                        self.cmd_defalut(input_cmd)
                else:
                    self.help()     #

    def help(self):
        print(ALL_CMD)

    def cmd_push(self, *args):      # 上传文件
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            file_name = cmd_split[1]
            if os.path.isfile(file_name):
                file_size = os.stat(file_name).st_size
                msg_dict = {
                    'action': 'push',
                    'filename': file_name,
                    'size': file_size,
                    'overridden': False
                }
                self.client.send(json.dumps(msg_dict).encode('utf-8'))
                # 为防止粘包，等服务器确认
                server_response = self.client.recv(1024)
                f = open(file_name, 'rb')
                for line in f:
                    self.client.send(line)
                else:
                    print('file upload success')
                    f.close()
            else:
                print(file_name, 'is not exist')


    def cmd_pull(self, *args):      # 下载文件
        # cmd_split = args[0]
        # if
        pass

    def cmd_defalut(self, *args):   # 如 ls, ifconfig, cd 等无数据交流的命令
        pass

if __name__ == '__main__':
    ftp_client = FTP_Client('localhost', 9999)
    ftp_client.run()
    # ftp_client.help()