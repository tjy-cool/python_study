#!/usr/bin/env python
# Funtion:      
# Filename:

class Dog(object):
    '''Dog类'''

    def __init__(self, name):
        self.name = name
        self.__animaltype = 'dog'

    def get_animal_type(self):
        return self.__animaltype

    def show_name(self):
        print('name: %s' % self.name)

d = Dog('xiaohei')
d.show_name()
print(d.get_animal_type())
d._Dog__animaltype = '狗'
print(d.get_animal_type())