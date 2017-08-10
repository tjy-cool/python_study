#!/usr/bin/env python
# Funtion:      
# Filename:

import urllib.request

file = urllib.request.urlopen("http://www.baidu.com")
data = file.read()
dataline = file.readlines()
# print(dataline)
# print(data)
fhandle = open("baidu.html", "wb")
fhandle.write(data)
fhandle.close()