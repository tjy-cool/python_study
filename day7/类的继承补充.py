#!/usr/bin/env python
# Funtion:      
# Filename:

class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print("person is talking...")
    # def talk(self, time):
    #     print('--- person is talking at the time', time)

class BlackPerson(Person):

    def __init__(self, name, age):
        # super(BlackPerson, self).__init__(name, age)
        Person.__init__(self,name,age)

    def talk(self, time):
        print('person is talking at the time', time)

p1 = Person('pppp',30)
p1.talk()

b1 = BlackPerson('bbbb', 23)
# b1.talk()
b1.talk('9:00')
