#/usr/bin/env python
# Author:tjy
'''
username = input("username:")
password =  input("password:")
print(username,password)
'''
Name = input("Name:")
Age = int(input("Age:"))        # integer
Job = input("Job:")
Salary = input("Salary:")

print(type(Age))

info = '''
---------- info of %s  ----------
Name: %s
Age: %d          
Job: %s
Salary: %s
''' % (Name, Name, Age, Job, Salary)

info2 = '''
---------- info2 of {_name}  ----------
Name: {_name}
Age: {_age}          
Job: {_job}
Salary: {_salary}
''' .format(_name=Name,
            _age=Age,
            _job=Job,
            _salary=Salary)

info3 = '''
---------- info2 of {0}  ----------
Name: {0}
Age: {1}          
Job: {2}
Salary: {3}
''' .format(Name, Age, Job, Salary)
print(info)
print(info2)
print(info3)