#!/usr/bin/env python
# Funtion:      
# Filename:


import socketserver
import json, hashlib, os
from conf import settings

user_info_dir = settings.BASE_DIR+'/db'+'/username_passwd/'

class MyTCPHandlers(socketserver.BaseRequestHandler):
    def handle(self):
        user_data = self.authentication()  # 用户认证
        if user_data:      # 登陆成功
            while True:
                try:
                    self.data = self.request.recv(1024).decode()
                    self.data = self.loads_from_json(self.data)
                    print(self.data)
                    cmd = self.data['func']
                    if hasattr(self, cmd):
                        func = getattr(self, cmd)
                        func(self.data)

                except ConnectionResetError as e:
                    if user_data['user_name'] is not'admin' and user_data is not None:
                        user_data['is_authenticated'] = 0   # 将登陆状态清0
                        with open(user_info_dir+'.json', 'w', encoding='utf-8') as f:
                            json.dump(user_data, f)
                    print('error:', e)


    def authentication(self):   # 用户登陆函数
        self.user_data = self.request.recv(1024).decode()
        if self.user_data == '':    # 表明已经断开了连接
            print('断开了一个连接')
        print(self.user_data)
        User_data = self.loads_from_json(self.user_data)
        username = User_data['user_name']
        passwd_md5 = User_data['passwd_md5']
        if username == 'admin':     # 系统用户
            if passwd_md5 == self.get_md5('admin'):
                print('admin login in successful!')
                self.request.send(b'OK')
                return User_data
            else:
                self.request.send(b'ERROR')
                return None

        else:       # 其他用户
            print(user_info_dir+username+'.json',   os.path.isfile(user_info_dir + username + '.json'))
            if os.path.isfile(user_info_dir+username+'.json'):   # 存在该用户数据
                with open(user_info_dir+username+'.json', 'r', encoding='utf-8') as f:    # 读取用户数据
                    user_db = json.loads(f.read())
                    if user_db['is_authenticated'] == -1:
                        user_db['is_authenticated'] = 0     # 本次登陆有效
                    elif user_db['is_authenticated'] == 1:
                        user_db['is_authenticated'] = 1
                    self.request.send(self.get_json(user_db).encode('utf-8'))  # 发送该用户的数据
                with open(user_info_dir + username + '.json', 'w', encoding='utf-8') as f:
                    user_db['is_authenticated'] = 1     # 针对其他设备来说来说，是已经在登陆过的了
                    json.dump(user_db, f, indent=4)
            else:   # 该用户不存在
                self.request.send(b'None')

    def add_user(self, Recv_dict):      # add_dict
        user_name = Recv_dict['user_name']
        # user_info_dir = settings.BASE_DIR + '/db' + '/username_passwd/'
        Recv_dict.pop('func')
        if os.path.isfile(user_info_dir+user_name+'.json'):
            self.request.send(b'EXIST')
        else:
            with open(user_info_dir+user_name+'.json', 'w', encoding='utf-8') as f:
                json.dump(Recv_dict, f, indent=4)   # 先删除 'func'的键值
            self.request.send(b'OK')

    def del_user(self, I_cmd):
        pass

    def query_user(self, I_cmd):
        pass

    def alter_uer(self, I_cmd):
        pass

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

    def loads_from_json(self, dict):
        return json.loads(dict)



def run():
    print("server is running...")
    server = socketserver.ThreadingTCPServer((settings.HOST, settings.PORT), MyTCPHandlers)
    server.serve_forever()
    server.server_close()


