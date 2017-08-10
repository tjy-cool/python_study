#!/usr/bin/env python
# Funtion:      
# Filename:

import urllib.request

filename = urllib.request.urlretrieve("http://edu.51cto.com",filename="51cto.html")
urllib.request.urlcleanup()
file = urllib.request.urlopen("http://www.51cto.com")
# print(file.info())
print(file.getcode())

sina_quote_url = urllib.request.quote("http://www.sina.com.cn")
print(sina_quote_url)
sina_url = urllib.request.unquote("http%3A//www.baidu.com.cn")
print(sina_url)