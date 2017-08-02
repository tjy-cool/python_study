#!/usr/bin/env python
# Funtion:      
# Filename:

import socket

server = socket.socket()
server.bind(("localhost", 1212))
server.listen(5)
while True:
    conn, addr = server.accept()
    while True:
        recv_data = conn.recv(1024)     # recv_data是 bytes类型
        print("recv_data", recv_data)
        print(recv_data.decode())
        if not recv_data:
            break
        conn.send(recv_data)            # "the client send data is".encode()

server.close()