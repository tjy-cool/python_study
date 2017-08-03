#!/usr/bin/env python
# Funtion:      
# Filename:

# 开发简单的FTP：
# 1. 用户登陆
# 2. 上传/下载文件
# 3. 不同用户家目录不同
# 4. 查看当前目录下文件
# 5. 充分使用面向对象知识

import socket

client = socket.socket()
client.connect(("localhost", 1234))

while True:
    username = input("username: ")
    client.send(username.encode())
    data = client.recv(1024)
    print(data.decode())

client.close()