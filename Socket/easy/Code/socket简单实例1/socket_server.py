#!/usr/bin/env python
# Funtion:      
# Filename:

import socket
server = socket.socket()

server.bind(('localhost', 6969))    # 绑定要监听的端口
server.listen(5)     # 监听

print("我要开始等电话了")
conn,addr = server.accept()     # 等电话打进来
# conn 就是客户端连接过来的，在服务端为其生成的一个连接实例
print("conn: %s\naddr: %s" % (conn, addr))

data = conn.recv(1024)
print("recv:", data.decode())
conn.send(data)

server.close()

