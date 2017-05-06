#!/usr/bin/env python
# Filename: login.py

import time
import sys

# 读取所有用户名和密码
user_passwd = []        # 用户名和密码保持为list
file = open('username_passwd.txt', 'r+', encoding='utf-8')     # 以只读方式打开文件
for line in file.readlines():               # file.readlines()为保存了文件所有数据的列表
    # print(line)
    temp1 = line.strip('\n')                # 去除换行符 \n
    temp2 = temp1.split(',')                # 以逗号为分隔符
    user_passwd.append(temp2)               # 将用户名和密码保存到user_passwd二维列表中
username_passwd = dict(user_passwd)         # 将二维列表转换为字典，存储用户名和密码

# 读取用户输入错误次数信息
err_info = []
f1 = open("err.txt", 'r+', encoding='utf-8')
for line in f1.readlines():
    temp = line.strip('\n').split(': ')
    err_info.append(temp)
# print(err_info)
err_info_dict = dict(err_info)

# 输入用户名密码
count_dict = dict.fromkeys(username_passwd, 0)  # 用count_dict保存用户输入错误密码的次数

while True:
    user = input("Please input username: ")     # 提示用户输入用户名
    if user in username_passwd.keys():          # 判断用户名是否在username_passwd字典的key里面
        # 若用户名在错误信息文本中，则已经被锁定了
        if user in err_info_dict.keys() :
            print("you have been locked at time :", err_info_dict[user])
            continue
        # 用户名不在错误信息文本中，则可以正常输入和登陆
        else :
            password = input("please input passwd: ")   # 提示用户输入密码

            # 认证成功后欢迎信息
            if username_passwd[user] == password:       # 判断密码是否与真实密码相等
                for i in range(6):
                    sys.stdout.write('-')
                    sys.stdout.flush()
                    time.sleep(0.5)
                print("\nwelcome! you are login...")      # 相等打印欢迎信息
                break                                   # 退出循环
            
            # 输入三次错误后锁定
            elif count_dict[user] == 2:                 # 当错误输入的次数达到三次时
                login_err_info_file = open("err.txt", 'a')
                localTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if err_info == [] :
                    login_err_info_file.write(user + ": " + localTime)
                else :
                    login_err_info_file.write("\n" + user + ": " + localTime)
                print("you have been locked...")
                login_err_info_file.close()
                break
            # 未达到三次，错误计数器 +1 
            else:
                count_dict[user] += 1
            print('You have input error passed %s times' % count_dict[user])
    else:
        issave = input("Do you want add a new user (y/n)? ")
        if(issave == 'y'):
            cur_passwd = input('Please input a passwd for the new user:')
            username_passwd[user] = cur_passwd
            file.write('\n' + user + ',' + cur_passwd)
        else :
            continue

file.close()
f1.close()

