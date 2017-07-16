#!/usr/bin/env python
# Funtion:      
# Filename:


def bulk(self):
    print("%s is yelling..." % self.name)

class Dog(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("%s is eating %s." % (self.name, food))

d = Dog("xiaohei")
choice = input(">>:").strip()
if hasattr(d, choice):
    getattr(d, choice)  # 删除

else:
    # setattr(d,choice, None)   # 属性
    # v = getattr(d,choice)
    # print(v)

    setattr(d, choice, bulk)
    func = getattr(d, choice)
    func(d)

