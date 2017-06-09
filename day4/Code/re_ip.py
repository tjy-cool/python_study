#!/usr/bin/env python
# Funtion:      
# Filename:

import re
ip_list = []
with open("ip.txt", 'r', encoding='utf-8') as f:
    for line in f.readlines():
        if re.search("(\d{1,3}\.){1,3}\d{1,3}", line) != None:
            ip_list.append(re.search("(\d{1,3}\.){1,3}\d{1,3}", line).group())

print(ip_list)
