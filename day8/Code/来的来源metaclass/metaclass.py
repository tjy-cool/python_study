#!/usr/bin/env python
# Funtion:      
# Filename:

# __new__ 是用来创建实例的

class MyType(type):
    def __init__(self,*args,**kwargs):
        print("Mytype __init__",*args,**kwargs)
    def __call__(self, *args, **kwargs):
        print("Mytype __call__", *args, **kwargs)
        obj = self.__new__(self)
        print("obj ",obj,*args, **kwargs)
        print(self)
        self.__init__(obj,*args, **kwargs)
        return obj
    def __new__(cls, *args, **kwargs):
        print("Mytype __new__",*args,**kwargs)
        print(type.__new__(cls, *args, **kwargs))
        return type.__new__(cls, *args, **kwargs)

print('here...')
class Foo(object,metaclass=MyType):
# class Foo(object):
#     __metaclass__ = MyType    # py2.x的写法
    def __init__(self,name):
        self.name = name
        print("Foo __init__")

    def __new__(cls, *args, **kwargs):
        print("Foo __new__",cls, *args, **kwargs)
        return object.__new__(cls)

f = Foo("Alex")
print("f",f)
print("fname",f.name)

