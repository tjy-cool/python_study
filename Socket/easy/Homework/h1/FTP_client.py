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
client.connect(("localhost", 6969))
login_flag = -1    # 登陆状态，-1表示没有登陆，0表示需要输入密码,1表示已经登陆
while True:
    if login_flag == -1:    # -1表示没有登陆，提示输入用户名
        send_data = input("username: ")
    if login_flag == 0: # 0表示需要输入密码，提示输入密码
        send_data = input("passwd: ")
    if login_flag == 1: # 1表示已经登陆,提示输入命令行
        send_data = input(">>: ")
    client.send(send_data.encode())     # 发送信息
    recv_data = client.recv(1024)       # 接受信息
    # if recv_data.decode() == "flag = 0":
    #
    #     if data == "passwd":
    #         print(data.decode())

client.close()