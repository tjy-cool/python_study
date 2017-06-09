#!/usr/bin/env python
# Funtion:      
# Filename:

# class A   # A为类
# a = A()   # a为对象

# A.__doc__       返回描述信息
# a.__doc__       同上 ,如 '该类是Dog类'

# a.__module__    返回当前操作的对象在哪个模块
# A.__module__     同上，如lib.aa

# A.__dict__    返回类里的所有属性，不包括实例属性
# a.__dict__    返回实例的所有属性，不包括类属性

# A.__class__   返回类名（包含包名），如lib.aa.C



class Dog():
    ''' 打印名字 '''
    def __init__(self, name):
        self.name = name
    def print_name(self):
        print(self.name)

    def __call__(self, *args, **kwargs):
        print('running call', args, kwargs)

    def __str__(self):
        return "<obj:%s>" % self.name

d = Dog('hello')

print(Dog.__doc__)
print(d.__doc__)
print(d.__module__)
print(Dog.__module__)

Dog('hello')()

print(Dog.__dict__)     # 返回类里的所有属性，不包括实例属性
print('dict', d.__dict__)   # 返回实例的所有属性，不包括类属性
# d(1,2,3, name='hao')

print(d.__hash__())
print(Dog.__bases__)

