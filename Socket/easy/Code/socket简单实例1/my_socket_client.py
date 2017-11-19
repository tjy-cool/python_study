#!/usr/bin/env python
# Funtion:      
# Filename:

import socket
client = socket.socket()    # self, family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None
client.connect(("localhost", 10000))
while True:
    send_str = input(">> ").strip()
    client.send(send_str.encode("utf-8"))
    data = client.recv(1024)    # 1024字节
    print("recv %s" % data.decode())

client.close()

