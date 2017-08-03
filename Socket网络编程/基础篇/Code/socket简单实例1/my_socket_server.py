#!/usr/bin/env python
# Funtion:      
# Filename:

import socket
server = socket.socket()
server.bind(("localhost", 1313))
server.listen()
print("等电话中。。。")
# conn是打电话的实例，addr是对方地址
conn,addr = server.accept()
print("conn: %s\naddr: %s" % (conn, addr))
while True:
    data = conn.recv(1024)
    print("recv: %s" % data.decode())
    conn.send(data*2)
server.close()
