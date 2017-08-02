#!/usr/bin/env python
# Funtion:      
# Filename:

import socket

client = socket.socket()

client.connect(("localhost", 1212))
while True:
    send_data = input(">>: ")
    if len(send_data) == 0:
        continue
    client.send(send_data.encode())
    recv_data = client.recv(1024)
    print("recv: %s" % recv_data.decode())

client.close()