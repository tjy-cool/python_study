#!/usr/bin/env python
# Funtion:      
# Filename:

import urllib.request

url = "http://blog.csdn.net/lovingprince/article/details/6627555"
file = urllib.request.urlopen(url)
file.getcode()