#!/usr/bin/env python
# Funtion:      
# Filename:

# 角色:学校、学员、课程、讲师
class School(object):
    ''' 学校类 '''
    def __init__(self, city):
        self.city = city

    def create_class(self):
        print('')
sh_school = School('Shanghai')
bj_school = School('Peking')

class Student(object):
    ''' 学员类 '''
    def __init__(self):
        pass

class Course(School):
    ''' 课程类 '''
    def __init__(self, city, period, price):
        super(Course,self).__init__(city)
        self.period = period
        self.price = price
    def show_course(self):
        print(self.city)

c1 = Course('sh', 12, 12334)
print(c1.city)

class Teacher(object):
    ''' 教师类 '''
    def __init__(self):
        pass


