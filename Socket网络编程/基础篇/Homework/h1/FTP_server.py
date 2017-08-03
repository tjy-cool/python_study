#!/usr/bin/env python
# Funtion:      
# Filename:

# 开发简单的FTP：
# 1. 用户登陆
# 2. 上传/下载文件
# 3. 不同用户家目录不同
# 4. 查看当前目录下文件
# 5. 充分使用面向对象知识

import socket,os

server = socket.socket()
server.bind(("localhost", 1234))
server.listen(5)

while True:
    conn, addr = server.accept()
    while True:
        username = conn.recv(1024)
        if username
        if not data:
            break
        conn.send("haha".encode())
        # res = os.popen(data).read()
        # conn.send(res.encode())

server.close()

