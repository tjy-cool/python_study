#!/usr/bin/env python
# Funtion:      
# Filename:

class Animal(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")

    # def talk2(self, obj):
    #     self.talk()


class Cat(Animal):
    def talk(self):
        return 'Meow'

class Dog(Animal):
    def talk(self):
        return "woof! woof!"

# a = Animal("lichaung")
# a.talk()

d = Dog("dd")
c = Cat("cc")
# Animal.talk(c)
# Animal.talk(c)

def animal_talk(obj):
    print(obj.talk())

animal_talk(c)
animal_talk(d)


