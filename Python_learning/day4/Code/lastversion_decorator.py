#!/usr/bin/env python
# Funtion:      
# Filename:

user, passwd = 'tjy', '1234'
def author(auth_type):
    def out_wripper(func):
        def wripper(*args, **kwargs):
            if auth_type == 'local':
                username = input('Input username: ').strip()
                password = input('Input password: ').strip()
                if username == user and password == passwd:
                    print('\033[31;1mUser has authentication\033[0m')
                    res = func(*args, **kwargs)
                    print('----after authentication ')
                    return res
                else :
                    exit('\033[31;1mInvalid username or password\033[32;1m')
            elif auth_type == 'ldap':
                print('----没有找到ldap。。。')
            else:
                print('invalid auth_type')

        return wripper
    return out_wripper


def index():
    print('\033[32;1mWelcome to index page! \033[0m')

@author(auth_type = 'local')     # home = wripper(home)
def home(x):
    print('\033[32;1mWelcome to home page! \033[0m')
    print(x)
    return x**2

@author(auth_type= 'local')
def bbs():
    print('\033[32;1mWelcome to bbs page! \033[0m')

index()
print(home(123))
bbs()