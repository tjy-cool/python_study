#!/usr/bin/env python
# Funtion:      
# Filename:

# 假设密码为 123
# 则shell下自动输入密码的语句为：
# echo "123" | sudo -S apt-get upgrade
# echo "123" | sudo -S apt-get install vim
# 可以查看标准文档 sudo --help

import subprocess
subprocess.Popen("echo '123' | sudo -S apt-get upgrade", shell=True)