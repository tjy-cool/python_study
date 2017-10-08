#!/usr/bin/env python
# Funtion:      
# Filename:

import socket, os

command = ['ls', 'ipconfig', 'dir', 'cd', 'ipconfig/all']
server = socket.socket()

server.bind(('localhost', 9999))
server.listen()

while True:
    conn, addr = server.accept()
    while True:
        recv_data = conn.recv(1024).decode()
        if recv_data not in command:
            conn.send("error command!".encode('utf-8'))
            continue
        res = os.popen(recv_data).read()
        if len(res) == 0:
            conn.send("该命令运行没有结果".encode('utf-8'))
            continue
        conn.send(res.encode('utf-8'))
