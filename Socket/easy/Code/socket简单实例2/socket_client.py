#!/usr/bin/env python
# Funtion:
# Filename:

# 客户端
import socket

client = socket.socket()     # 定义协议类型，同上生成socket连接对象
client.connect(('localhost',6969))

while True:
    msg = input(">>:").strip()
    if len(msg) != 0:   # 发不了空
        client.send(msg.encode('utf-8'))
        data = client.recv(10240000)
        print("recv:", data.upper().decode())

        f = open("video.avi", 'wb')
        f.write(data)
        f.close()

client.close()

