#!/usr/bin/env python
# Funtion:      
# Filename:

class SchoolMember(object):
    '''学校成员基类'''
    member = 0
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.enroll()

    def enroll(self):
        '''注册'''
        print("just enrolled a new school member [%s]" % self.name)
        SchoolMember.member += 1

    def tell(self):
        print("------ %s info ------" %self.name)

    def __del__(self):
        print("开除了[%s]... "% self.name)
        SchoolMember.member -= 1

class School(object):
    '''学校类'''
    def __init__(self):
        pass
    def open_branch(self, addr):
        print("openning a new branch in ", addr)

class Teacher(SchoolMember, School):
    '''讲师类'''
    def __init__(self, name, age, sex, salary, course):
        # SchoolMember.__init__(self, name, age, sex)   # 经典类写法
        super(Teacher, self).__init__(name, age, sex)   # 新式类写法
        self.salary = salary
        self.course = course
        self.amount = 0

    def teaching(self):
        print("Teacher [%s] is teaching [%s]" %(self.name, self.course))

class Student(SchoolMember):
    '''学生类'''
    def __init__(self, name, age, sex, course, tuition):
        SchoolMember.__init__(self, name, age, sex)
        self.course = course
        self.tuition = tuition  # fee

    def pay_tuition(self,amount):
        print("student [%s] has just paid [%s]" %(self.name, amount))
        self.amount += amount


t1 = Teacher("Wusir", 27, "M", 3000, "python")
s1 = Student("Haitao", 29, "M", "python", 30000)
s2 = Student("Lichuang", 12, "M", "pys16", 11000)

t1.open_branch("shanghai")
print(SchoolMember.member)
print(t1.member)