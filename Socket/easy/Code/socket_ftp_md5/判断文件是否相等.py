#!/usr/bin/env python
# Funtion:      
# Filename:
import hashlib

# source_file = 'vspd.zip'
file1 = 'NIVISA1550full.exe'
file2 = file1+'.new'

def get_file_md5(file_name):
    file_md5 = hashlib.md5()
    with open(file_name, 'rb') as f:
        for line in f:
            file_md5.update(line)
        print(file_md5.hexdigest())
        return file_md5
file1_md5 = get_file_md5(file1)
file2_md5 = get_file_md5(file2)

print(file1_md5)
print(file2_md5)