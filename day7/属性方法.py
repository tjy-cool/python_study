#!/usr/bin/env python
# Funtion:      
# Filename:

import os

class Dog(object):
    food = 'water'
    def __init__(self, name):   # self 为对象，cls为类
        self.name = name
        self.n = '123'
        self.__food = 'fish'
    # @staticmethod   #  实际上跟类没什么关系了，只是需要利用类来调用而已
    # @classmethod      # 只能访问类的共有属性，不能访问普通属性（即成员变量）
    @property  # attribute
    def eat(self):
        print("%s is eating %s" % (self.name, self.__food))

    @eat.setter
    def eat(self, food):
        print('set to food:', food)
        self.__food = food

    @eat.deleter
    def eat(self):
        del self.__food
        print('self.food has been del')
    #
    # def talk(self):
    #     print('%s is talking' %self.name)

d1 = Dog('Bagong')
d2 = Dog('haha')

d1.eat
d2.eat
d1.eat = 'baozi'
d1.eat
#
# print(d1.eat)
#
del d1.eat
# d1.eat
# print(d1.eat)

# del d1.name
# print(d1.name)

# del d1.eat
