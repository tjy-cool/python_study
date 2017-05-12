#!/usr/bin/env python
# Funtion:      
# Filename:

import sys
import os
print(sys.path)

pre_path = os.path.abspath('../')
sys.path.append(pre_path)
print(''.center(50,'='))

# print(sys.path)

print(os.getcwd())

sys.stdout.write('please:')
val = sys.stdin.readline()
print(val)