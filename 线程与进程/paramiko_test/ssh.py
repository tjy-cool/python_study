#!/usr/bin/env python
# Funtion:      
# Filename:

import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# 连接服务器
ssh.connect(hostname='cl.salt.com', port=22, username='lemaker', password='lemaker')
# 执行命令
stdin, stdout, stderr = ssh.exec_command('df')      #不能执行top命令，只能执行top -bn 1
# stdin 标准输入， 即输入的命令
# stdout 标准输出， 即输出的命令
# stderr 标准错误， 即执行命令错误的返回值

# 获取命令结果
res, err = stdout.read(), stderr.read()
result = res if res else err  # 返回的是bytes格式
print(result.decode())


# 关闭连接
ssh.close()