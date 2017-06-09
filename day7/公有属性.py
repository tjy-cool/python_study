#!/usr/bin/env python
# Funtion:      
# Filename:

class Role(object):
    nationlity = 'Japan'

    def __init__(self, name, role, weapon, life_value = 100, money=15000):
        self.name = name    # 成员属性
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money
        self.__heart = 'Normal'     # 私有属性，变量名前需要有两个下划线__, 相当于private
        self.__aa = 'haha'

    def shot(self):
        print("%s is shooting..." % self.name)

    # def shot(self, per):
    #     print('%s is shotting at %s' % self.name, per)

    def get_heart(self):    #对外部提供只读访问接口
        return self.__heart

    def got_shot(self):
        print("ah...,I got shot...")
        self.__heart = 'Die'
        print(self.__heart)

r1 = Role("HaiTao", "警察", "B22")
r2 = Role("lichuang", "警犬", "B13")

r1.shot()

Role.nationlity = 'Thailand'
r1.nationlity = 'CN'
# print(r1._Role__nationlity)

print('============= after change: ============')
print(id(r1), id(r1.nationlity))
print(id(r2), id(r2.nationlity))

del r1.nationlity
print("============== after del: ===============")
print(id(r1), id(r1.nationlity))
print(id(r2), id(r2.nationlity))


# def shot1(self):
#     print("This is my own shot", self.name)
#
# r1.shot = shot1
# r1.shot(r1)
