#!/usr/bin/env python
# Funtion:
# Filename:

import socket
# self, family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None
client = socket.socket()
client.connect(("192.168.6.128", 5025))
while True:
    send_str = input(">> ").strip()
    client.send(send_str.encode("utf-8"))
    data = client.recv(1024)    # 1024字节
    print("recv %s" % data.decode())

client.close()
