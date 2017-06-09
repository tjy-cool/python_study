#!/usr/bin/env python
# Funtion:      
# Filename:

print(50*'-')

print(len(('\033[32;1m%s\033[0m' % '').center(100,'-')))
print(('\033[32;1m%s\033[0m' % '').center(50,'-'))
print(len('---------------------------------------------'))

print(len(('\033[32;1m%s\033[0m' % 'a').center(100,'-')))
print(('\033[32;1m%s\033[0m' % 'a').center(50,'-'))
print(len('----------------------a----------------------'))

print(len(('\033[32;1m%s\033[0m' % 'afsdfsfdsfsafb').center(50,'-')))
print(('\033[32;1m%s\033[0m' % 'aafsdfsfdsfsafbb').center(50,'-'))

print(len(('\033[32;1m%s\033[0m' % '中').center(50,'-')))
print(('\033[32;1m%s\033[0m' % '中').center(50,'-'))

print(len(('\033[32;1m%s\033[0m' % '中国').center(100,'-')))
print(('\033[32;1m%s\033[0m' % '中国的国土不容侵犯').center(100,'-'))
print(len('----------------------中----------------------'))