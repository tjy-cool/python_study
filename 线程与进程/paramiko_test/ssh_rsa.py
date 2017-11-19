#!/usr/bin/env python
# Funtion:      
# Filename:

import paramiko

private_key = paramiko.RSAKey.from_private_key('/home/auto/.ssh/id_rsa')

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='10.0.0.41', port=22, username='wupeiqi', pkey = private_key)

# 执行命令
stdin, stdout, stderr = ssh.exec_command('df;ifconfig')
# 获取命令结果
result = stdout.read()
print(result.decode())

