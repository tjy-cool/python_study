#!/usr/bin/env python
# Funtion:      
# Filename:

import socket, json
import hashlib
from conf import settings

class FTP_Client(object):
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT
        self.client = socket.socket()
        # try:
        self.client.connect((HOST, PORT))
        # except ConnectionRefusedError as e:
        #     print('错误代码 4,', settings.MYERRORS[4])


    def run(self):
        user_data = self.authentication()
        print(user_data)
        while True:
            pass

    def authentication(self):
        '''
        用户登陆函数
        :return:
        '''
        Max_count = 3
        input_count = 0
        while input_count < Max_count:
            username = input('user name: ').strip()  # 输入用户名
            if len(username) == 0:  # 用户名不能为空
                print('Invalid username, please input username again')
                continue
            else:
                settings.USER_DATA['user_name'] = username
            passwd = input('passwd: ').strip()  # 输入密码

            md5 = hashlib.md5()  # 密码进行md5加密处理
            md5.update(bytes(passwd, 'utf-8'))
            passwd_md5 = md5.hexdigest()
            settings.USER_DATA['passwd_md5'] = passwd_md5
            send_data = json.dumps(settings.USER_DATA)  # 将用户数据格化为json格式
            print(type(send_data), send_data)
            self.client.send(send_data.encode('utf-8'))
            recv_user_data = self.client.recv(1024).decode()  # 接收到的用户数据
            if recv_user_data['locked'] == 1:   # 用户已经被锁住了
                print('user [%s] has been input more than three error password' % recv_user_data['user_name'])
                return 3
            if recv_user_data['is_authenticated'] == 1: # 1表示已经在其他设备登陆中
                print('user [%s] has logined in other device' %recv_user_data['user_name'])
                return 0
            elif recv_user_data['is_authenticated'] == -1: # -1表示没有任何人登陆
                input_count += 1
                if input_count == 2:
                    print('user [%s] has been locked this time' % recv_user_data['user_name'])
                    return 3
                else:
                    print('invilid username or password')
            elif recv_user_data['is_authenticated'] == 0:   # 0表示正常登陆
                return recv_user_data



def run():
    print('client is running ...')
    client = FTP_Client(settings.HOST, settings.PORT)
    client.run()
