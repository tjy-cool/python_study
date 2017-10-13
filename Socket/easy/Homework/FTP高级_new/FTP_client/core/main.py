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
        user_db = self.authentication()
        if isinstance(user_db, dict):     # 返回的数据是字典格式
            while True:
                cmd  = input("%s/home>"%(user_db['user_name']))
                self.client.send(b'')
                pass


    def authentication(self):
        '''
        用户登陆函数
        :return: 接受到来自客户端的用户数据
        '''
        Max_count = 3
        input_count = 0
        user_data = settings.USER_DATA
        while input_count < Max_count:
            username = input('user name: ').strip()  # 输入用户名
            if len(username) == 0:  # 用户名不能为空
                print('Invalid username, please input username again')
                continue
            user_data['user_name'] = username
            passwd = input('passwd: ').strip()  # 输入密码
            passwd_md5 = self.get_md5(passwd)

            user_data['passwd_md5'] = passwd_md5
            send_data = self.get_json(user_data)  # 将用户数据格化为json格式
            self.client.send(send_data.encode('utf-8'))     # 将用户数据发送给服务器
            recv_user_data = self.client.recv(1024).decode()  # 接收到的用户数据

            if  recv_user_data['user_name'] == None or recv_user_data['passwd_md5'] == None:
                print('invalid username or password,try again!')
                input_count += 1
            elif recv_user_data['locked'] == 1:   # 用户已经被锁住了
                exit('user [%s] has been locked' % recv_user_data['user_name'])
            elif recv_user_data['is_authenticated'] == 1: # 1表示已经在其他设备登陆中
                exit('user [%s] has logined in other device' %recv_user_data['user_name'])
            elif recv_user_data['is_authenticated'] == 0:   # 0表示正常登陆
                print('[%s] login successful...')
                return recv_user_data
        else:
            exit('Too many times attempt...')

    def get_md5(self, src_str):
        '''
        对输入的源字符串计算md5值，并返回
        :param src_str: 待计算md5的字符串
        :return: 计算出来的md5值
        '''
        md5 = hashlib.md5()  # 密码进行md5加密处理
        md5.update(bytes(src_str, 'utf-8'))
        return md5.hexdigest()
    def get_json(self, src):
        # 将数据格式化为json格式
        return json.dumps(src)


def run():
    print('client is running ...')
    client = FTP_Client(settings.HOST, settings.PORT)
    client.run()
