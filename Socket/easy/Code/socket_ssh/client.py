#!/usr/bin/env python
# Funtion:      
# Filename:

import socket
client = socket.socket()

client.connect(("localhost", 9999))

while True:
    command = input("请输入命令：").strip()
    if len(command) == 0:
        continue
    client.send(command.encode('utf-8'))

    recv_data = client.recv(1024)
    print("recv: \n", recv_data.decode())

client.close()