#!/usr/bin/env python
# Funtion:      
# Filename:

import pickle

class School(object):
    ''' 学校类 '''
    def __init__(self, city):
        self.city = city
    def __setitem(self, key, value):
        if key == "class":
            self.classes = value
            
class Lesson(object):
    ''' 课程类 '''
    def __init__(self):
        pass
    
    def __setitem__(self, key, value):
        if key == "class":
            pass

class Stu(object):
    ''' 学员类 '''
    def __init__(self,school):
        self.school = school
    def __setitem__(self, key, value):
        if key == "class":
            self.classes = value
                
# if __name__ == "__main__":
#     print("\t1  Student\n"
#           "\t2  Teacher\n"
#           "\t3  administrator".expandtabs(8))
#     role = input(">> ").strip()
#     if role == "1":
#         print("Hello Student")
#     elif role == "2":
#         print("Hello Teacher")
#     elif role == "3":
#         print("Hello administrator")
#     else:
#         print("invalid input")


s_bj = School("BJ")
print(s_bj.city)
# s_bj["class"] =