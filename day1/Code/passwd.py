#/usr/bin/env python
# Author:tjy
import getpass

_username = "tjy"
_password = "abcd1234"
username = input("username:")
# password = input("password:")
password = getpass.getpass("password:")

if _username == username and _password == password:
    print("welcome user {name} login..." .format(name = username))
else:
    print("username or password error")
# print(username, password)