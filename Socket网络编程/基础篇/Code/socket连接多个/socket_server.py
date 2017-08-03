#!/usr/bin/env python
# Funtion:      
# Filename:

import socket,os

server = socket.socket()
server.bind(("localhost", 1313))
server.listen(1)
while True:
    conn, addr = server.accept()
    while True:
        recv_data = conn.recv(1024)     # recv_data是 bytes类型
        print("recv_data", recv_data)
        print(recv_data.decode())
        if not recv_data:
            break
        res = os.popen(recv_data.decode()).read()
        conn.send(res.encode())            # "the client send data is".encode()

server.close()