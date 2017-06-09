#!/usr/bin/env python
# Funtion:      
# Filename:

class Foo(object):       # 创建类的普通方式
    def __init__(self,name):
        self.name = name

f = Foo('alex')
print(type(f), type(Foo))

###########################################################
# 类的起源来自type
def func(self):
    print('hello Alex')
def __init__(self, name, age):
    self.name = name
    self.age = age
Foo1 = type('Foo1',(object,), {'talk': func,
                        '__init__': __init__})      # type为类的类
print(type(Foo1))
f1 = Foo1('alex', 28)
f1.talk()
