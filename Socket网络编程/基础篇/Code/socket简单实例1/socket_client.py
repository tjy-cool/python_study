#!/usr/bin/env python
# Funtion:      
# Filename:

# 客户端
import socket

client = socket.socket()     # 定义协议类型，同上生成socket连接对象
client.connect(('localhost',6969))

client.send('Hello world，我的名字是tjy!'.encode('utf-8'))
data = client.recv(1024)
print("recv:", data.upper().decode())

client.close()

