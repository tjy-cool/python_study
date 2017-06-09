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
    delattr(d, choice)  # 删除
    # func = getattr(d, choice)     # 方法
    # func('wahaha')

    # attr = getattr(d, choice)       # 属性
    # setattr(d, choice, 'hao123')
    # print(attr)

elif choice == "talk":
    setattr(d, choice, bulk)    # 动态装配 方法
    d.talk(d)

else:
    setattr(d, choice, 22)
    print(getattr(d,choice))

print(d.name)