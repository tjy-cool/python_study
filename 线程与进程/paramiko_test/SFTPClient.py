#!/usr/bin/env python
# Funtion:      基于用户名密码上传下载
# Filename:

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.1.10', port=22, username='pi', password='22')
stdin, stdout, stderr = ssh.exec_command('df')
result = stdout.read()
ssh.close()

