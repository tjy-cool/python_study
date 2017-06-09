#/usr/bin/env python
# Author:tjy
'''
file = open("username_passwd.txt", 'r')
line = file.readline()
while line:
    print(line) ,
    line = file.readline()
file.close()
'''

'''
for line in open("username_passwd.txt", 'r') :
    print(line)
'''


file = open("username_passwd.txt", 'r')
lines = file.readlines()
print(lines)
for line in lines :

    print(line)
    