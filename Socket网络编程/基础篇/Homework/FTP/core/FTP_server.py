#!/usr/bin/env python
# Funtion:      
# Filename:

# 开发简单的FTP：
# 1. 用户登陆   #可以完成
# 2. 上传/下载文件
# 3. 不同用户家目录不同
# 4. 查看当前目录下文件
# 5. 充分使用面向对象知识

import socket,os

class Ftp_server(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def run_server(self):
        server = socket.socket()
        server.bind((self.ip, self.port))
        server.listen(5)
        while True:
            conn, addr = server.accept()
            while True:
                command = conn.recv(1024)
                if command.decode() == "login":  # 登陆
                    self.in_login(conn)    # 登陆

                elif command == "download": # 下载文件
                    self.download(conn)
                elif command == "upload":   # 上传文件
                    self.upload()
                elif command == "ls":       # 显示文件目录
                    self.ls(conn)

    def read_User_Passwd(self, input_user, input_passwd):
        with open("username_passwd.txt", 'r+', encoding="utf-8") as f:
            for line in f:
                username = line.split(",")[0].strip()
                passwd = line.split(",")[1].strip()
                if input_user == username and input_passwd == passwd:
                    return username     # 如果用户名和密码正确返回用户名，如果不正确返回None
        return None


    def in_login(self, conn):
        username = conn.recv(1024)
        passwd = conn.recv(1024)
        login_user = self.read_User_Passwd(username.decode(), passwd.decode())
        if login_user != None:
            conn.send(login_user.encode())
            print(login_user)
        else:
            conn.send("None".encode())

    def download(self, conn):
        pass

    def upload(self):
        pass

    def ls(self, conn):

        pass


        # while True:
        #     conn, addr = server.accept()
        #     login_flag = -1    # 登陆状态，-1表示没有登陆，0表示需要输入密码,1表示已经登陆
        #     while True:
        #         data = conn.recv(1024)
        #         print(login_flag)
        #         if not data:    # 没有数据表示已经断开连接
        #             break
        #         else:
        #             if login_flag == -1: # 没有登陆，则data为用户名
        #                 user_pw = []
        #                 with open("username_passwd.txt", "r+", encoding="utf-8") as f:
        #                     for line in f:
        #                         username = line.split(",")[0].strip()
        #                         passwd = line.split(",")[1].strip()
        #                         user_pw.append([username,
        #                                         passwd])
        #                         print(username)
        #                         if data.decode() == username:    # 存在该用户
        #                             login_flag = 0
        #                             conn.send("passwd".encode())  # 发送需要接收密码
        #                             break
        #                         else:
        #                             conn.send("没有该用户名，请重新输入！".encode())
        #             if login_flag == 0: # 0表示用户名正确，需要输入密码
        #                 # conn.send("passwd".encode())  # 发送需要接收密码
        #                 passwd = conn.recv(1024)  # 等待接收密码
        #
        #         if login_flag == 1: # 已经登陆，则data为命令
        #                 pass
        #
        #         if data.decode() == "tjy":
        #             conn.send("你已经成功登陆了".encode())
        #             # res = os.popen(data).read()
        #             # conn.send(res.encode())
        # server.close()




ftp_server = Ftp_server("localhost", 6969)
ftp_server.run_server()
