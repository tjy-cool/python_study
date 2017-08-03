#!/usr/bin/env python
# Funtion:      
# Filename:
# 格式：类名 = type('类名',(父类，)，{'方法名'：方法的内存地址})

# 总结：类 是由 type 类 实例化产生的
# 值得注意的是，新式类的写法，在继承父类那边，你继承一个父类后面就要加一个逗号，
# 加逗号，它就把它当做一个元组，不加逗号，就是一个值了

def func(self):
    print("hello {}".format(self.name))

def __init__(self, name):
    self.name = name

Foo = type("Foo", (object,),{"talk":func, "__init__":__init__})

f = Foo("tjy")
f.talk()