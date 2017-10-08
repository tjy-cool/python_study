#!/usr/bin/env python
# Funtion:      
# Filename:

import socket
import os

server = socket.socket()
server.bind(('localhost', 9999))
server.listen()

while True:
    conn, addr = server.accept()
    while True:
        recv_cmd = conn.recv(1024).decode()
        if recv_cmd.startswith("get "):
            file_name = recv_cmd.split(' ')[1]
            print(file_name)
            if not os.path.isfile(file_name):
                conn.send(b'file not exist')
            else:
                file_size = os.stat(file_name).st_size
                print(file_size)
                conn.send( (str(file_size)).encode('utf-8'))    # 发送文件大小到客户端

                comfirmed_info = conn.recv(1024)
                f = open(file_name, 'rb')
                for line in f:
                    conn.send(line)
                print('send done...')
                f.close()

server.close()
