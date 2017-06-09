#!/usr/bin/env python
# Funtion:      
# Filename:

import os
os.system('dir')      #输出命令结果到屏幕，返回命令执行状态, 正确返回0，不正确返回1
os.popen('dir').read()    # 会保存命令运行结果

# py 2.7中
# import commands       # only support linux
# commands.getstatusoutput("dir")
#

# linux 中
# subprocess
import subprocess
subprocess.run('df','-h')
subprocess.run('df -h | grep sda1', shell = True)

res = subprocess.Popen("ifconfig|grep 192", shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
res.stdout.read()   # 返回输出结果

# 执行需要消耗长时间的命令
res1 = subprocess.Popen("sleep 10;echo 'Hello'", shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
print(res1.poll())  # 上面的语句没有运行完就返回None,运行完了就返回0
# print(res1.wait())  #  与res1.poll()的区别是：该语句会一直等待直到运行完了返回0
res1.stdout.read()  # 会卡住，需要用poll()去检测

# res.terminate() 结束进程
# 执行需要消耗长时间的命令
res2 = subprocess.Popen("sleep 10;echo 'Hello'", shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
res2.terminate()

# res.communicate() 连续输入命令
res2 = subprocess.Popen("python3", shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
res2.stdin.write(b"print('1')")
res2.stdin.write(b"print('2')")
res2.stdin.write(b"print('3')")
res2.stdin.write(b"print('4')")
out_error_list = res2.communicate(timeout=10)
print(out_error_list)

subprocess.Popen('sudo apt-get upgrade', shell=True)
