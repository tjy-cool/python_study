#!/usr/bin/env python
# Funtion:      
# Filename:

import socket, hashlib
import os

client = socket.socket()
# client.connect(('localhost', 9999))
client.connect(('192.168.1.200', 9999))


while True:
    cmd = input(">> ").strip()
    if cmd == '':
        continue
    client.send(cmd.encode('utf-8'))
    tol_file_size = client.recv(1024).decode()
    if tol_file_size == 'file not exist':
        print('file not exist')
    else:
        client.send('OK'.encode('utf-8'))
        received_size = 0
        print(tol_file_size)
        tol_file_size = int(tol_file_size)
        file_md5 = hashlib.md5()
        f = open(cmd.split(' ')[1]+'.new', 'wb')
        while tol_file_size -  received_size > 0:
            if tol_file_size -  received_size > 1024:
                size = 1024
            else:
                size = tol_file_size - received_size
            data = client.recv(size)
            file_md5.update(data)
            received_size += len(data)
            # print(data.decode())
            f.write(data)
        else:
            print('recv done...')
            recv_md5 = client.recv(1024).decode()
            if file_md5.hexdigest() == recv_md5:
                print('received file completely...')
            else:
                print('file has broked...')
            f.close()
client.close()