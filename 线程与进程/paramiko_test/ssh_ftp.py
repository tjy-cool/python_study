#!/usr/bin/env python
# Funtion:      
# Filename:

# netstat -tulnp        # 查询
# netstat -tulnp|grep 22    # 查询是否有22端口
# netstat -tulnp | grep ssh

# vim /ect/ssh/sshd-config      #进入编辑
# 输入/Root   ，查找Root
# 更改 Permit:RootLogin yes  ，如果为without-password 则无需更改

# 重新启动ssh的命令：
# service sshd restart

# ssh登陆 如果端口号不是默认的22，若为52113，则应该为
# ssh pi@192.168.1.200 -p52113

# 传送文件
# scp -rp -P52113 oldgirl.txt pi@192.168.1.200

import paramiko

# 创建
transport = paramiko.Transport(('hostname', 22))
transport.connect(username='lemaker', password='lemaker')

sftp = paramiko.SFTPClient.from_transport(transport)

# 将location.py 上传至服务器 /tmp/test.py
sftp.put('/tmp/localton.py', '/tmp/test.py')
# 将remove_path 下载到local_path
sftp.get('remove_path', 'local_path')