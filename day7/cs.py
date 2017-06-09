#!/usr/bin/env python
# Funtion:      
# Filename:

import time

class Role(object):
    def __init__(self, name, role, weapon, life_value = 100, money=15000):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money
        self.__heart = 'Normal'     # 私有属性，变量名前需要有两个下划线__

    def shot(self):
        print("%s is shooting..." % self.name)

    def get_heart(self):    #对外部提供只读访问接口
        return self.__heart

    def got_shot(self):
        print("ah...,I got shot...")
        self.__heart = 'Die'
        print(self.__heart)

    def __del__(self):
        print("del ...function...")

    def buy_gun(self, gun_name):
        print("Just bought %s" % gun_name)
        self.weapon = gun_name

r1 = Role('TJY', 'police', 'AK47')
r2 = Role('Jick', 'terrorist', 'B22')

r1.got_shot()
r1.shot()
r2.buy_gun('B46')

del r1
time.sleep(2)
print("haha")
# r1._Role__heart     # 强制访问私有属性



