#!/usr/bin/env python
# Funtion:      
# Filename:

import os

class Dog(object):

    name = '123'    # 类的公有属性
    def __init__(self, name):
        self.name = name

    # @staticmethod   #  实际上跟类没什么关系了
    @classmethod      # 只能访问类的共有属性，不能访问普通属性（即成员变量）
    def eat(self,food):
        print("%s is eating %s" % (self.name, food))
        print(self.name)

    def talk(self):
        print('%s is talking' %self.name)

d1 = Dog('Bagong')
d2 = Dog('haha')

d1.eat('fish')
