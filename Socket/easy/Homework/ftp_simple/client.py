#!/usr/bin/env python
# Funtion:      
# Filename:

import socket, os, hashlib

ALL_CMD = ['ls', 'push', 'pull', 'cd', 'ifconfig', 'df']

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
                cmd = input_cmd.split(' ')[0]
                param = input_cmd.split(' ')[1:-1]
                if cmd in ALL_CMD:
                    if hasattr(self, 'cmd_'+cmd):
                        obj = getattr(self, 'cmd_'+cmd)
                        obj(cmd)
                    else :
                        self.cmd_defalut(cmd)

    def help(self):
        print(ALL_CMD)

    def cmd_push(self, *args):

        pass
    def cmd_pull(self, *args):
        pass
    def cmd_defalut(self, *args):
        pass

if __name__ == '__main__':
    ftp_client = FTP_Client('localhost', 22)
    # ftp_client.run()
    ftp_client.help()