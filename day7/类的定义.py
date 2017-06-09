#!/usr/bin/env python
# Funtion:      
# Filename:

class Dog(object):

    def __init__(self, name):   # 构造函数，构造方法，  初始化方法
        self.name = name

    def sayhi(self):    # 类的方法
        print(self)
        print('hello, I am a dog.my name is ',self.name)

    def eat(self,food):
        print("%s is eating %s" %(self.name, food))

print(Dog)
d = Dog("lichuang")     # 相当于Dog(d, "lichuang")   # 实例化后产生的对象 叫 实例
print(d)
d.sayhi()   # d.sayhi(d)

d.eat("fish")