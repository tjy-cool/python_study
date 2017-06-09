#!/usr/bin/env python
# Funtion:      
# Filename:

class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print("person is talking...")

def WhitePerson(Person):
    pass

class BlackPerson(Person):

    def __init__(self,name,age,strength):     # 先继承，后重构
        Person.__init__(self, name,age)     # 此时，self = b
        self.strength = strength

    def talk(self):     # 父类函数重写
        print("Black is talking...")

    def walk(self):     # 成员函数
        print("is walking ...")


b = BlackPerson("wei er smith", 30, 10)
b.talk()
b.walk()

