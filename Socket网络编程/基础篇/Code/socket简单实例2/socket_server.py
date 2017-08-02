#!/usr/bin/env python
# Funtion:      
# Filename:

import os
import socket
server = socket.socket()

server.bind(('localhost', 6969))    # 绑定要监听的端口
server.listen(5)     # 监听， 一般写5个
while True:
    print("等电话中...")
    # conn 就是客户端连接过来的，在服务端为其生成的一个连接实例
    conn,addr = server.accept()     # 等电话打进来
    print("电话来了...")
    while True:
        data = conn.recv(1024)
        print("recv:", data.decode())
        if not data:
            print("client has lost...")
            break

        # res = os.popen(data).read()   # 执行命令
        # conn.send(res)                # 将命令执行结果返回

        # conn.send(data.upper())

        f = open('oldboy-1.avi','rb')
        data = f.read()
        conn.sendall(data)

server.close()

