#!/usr/bin/env python
# Funtion:      
# Filename:

# name = [1,2,3]
# try:
#     day = 1
# except IndexError as e:
#     print(e)
# except KeyError as e:
#     print(e)
# except (IOError , ImportError) as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     print("No Error")
# finally:
#     print("No matter Error or not would run here!")

'''
name = [1,2,3]
data = {"Year":"2017", "Month":"7"}
# print(data["Day"])
try:
    print(name[3])      # 这边已经出现异常IndexError ，所以直接跳出code，跳到KeyError 下去处理
    print(data["Day"])
# except IndexError as e:
#     print(e)
# except KeyError as e:
#     print(e)
except (IndexError, KeyError) as e:
    print(e)
'''



# class TjyError(Exception):
#     def __init__(self, message):
#         self.message = message
#
#     def __str__(self):
#         return self.message
# try:
#     raise TjyError("数据库连接不上了")
# except TjyError as e:
#     print(e)

# class Time(object):
#     print("in it")
#     def __init__(self, hour, minute, second):
#         print("in init")
#         self.hour = hour
#         self.minute = minute
#         self.second = second
#     def __str__(self):
#         print("hahahaha")
#         return "%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second)
#
# print("out ")
# tim = Time(2, 34, 32)
# print(tim)
# print(tim.hour)

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
    def __str__(self):
        return '(Student: %s, %s, %s)' % (self.name, self.gender, self.score)
    __repr__ = __str__

s = Student('Bob', 'male', 88)
print(s)