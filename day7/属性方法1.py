#!/usr/bin/env python
# Funtion:      
# Filename:

class Dog(object):
    def __init__(self,name, age):
        self.name = name
        self.age = age
        self.__food = 'fish'

    @property
    def eat(self):
        print('{0} is eating {1}'.format(self.name, self.__food))

    @eat.setter
    def eat(self, food):
        print('set to food:', food)
        self.__food = food

    @eat.deleter
    def eat(self):
        del self.__food
        print('food 变量删除完毕')

    @eat.getter
    def eat(self):
        return self.__food
    property

d1 = Dog('bagong', 1)
d1.eat

d1.eat = 'water'
d1.eat

print(d1.eat)

del d1.eat
print('111')


class C(object):
    def __init__(self):
        self._x = '123'
    def getx(self): return self._x
    def setx(self, value): self._x = value
    def delx(self): del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")

c = C()
c.setx = '222'
a = c.getx
print(a())

