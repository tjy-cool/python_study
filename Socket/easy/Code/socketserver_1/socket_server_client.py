#!/usr/bin/env python
# Funtion:      
# Filename:

import socket
client = socket.socket()
client.connect(('192.168.1.200', 9999))

while True:
    cmd = input(">> ").strip()
    if cmd == '':
        continue
    client.send(cmd.encode('utf-8'))
    cmd_res = client.recv(1024)
    print( cmd_res.decode('utf-8', 'ingore'))

client.close()