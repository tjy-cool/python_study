#!/usr/bin/env python
# Funtion:      
# Filename:

# @staticmethod 为静态方法
# 作用：取消与类的关联，具体表现为不用必须传入参数self了，
# 但是如果传了self，会把self当成普通的位置参数

import sys
sys.__loader__.load_module()

class Dog(object):
    def __init__(self, name):
        self.name = name

    @staticmethod   #  实际上跟类没什么关系了
    def eat(self,food):
        print("%s is eating %s" % (self.name, food))
        print(self.name)

    def talk(self):
        print('%s is talking' %self.name)

d1 = Dog('Bagong')
d2 = Dog('haha')

d1.eat(d2, 'fds.txt')
