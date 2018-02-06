#!/usr/bin/env python
# Funtion:
# Filename:

import socket
import os
server = socket.socket()
server.bind(("localhost", 5025))
server.listen()
print("等电话中。。。")
# conn是打电话的实例，addr是对方地址
conn, addr = server.accept()
print("conn: %s\naddr: %s" % (conn, addr))
while True:
    data = conn.recv(1024)
    if data.decode() == "ls":
        data = os.popen("dir").read()
        print(data)
        conn.send(data.encode())
    else:
        print("recv: %s" % data.decode())
        conn.send(data)
        print('send ok')
server.close()
