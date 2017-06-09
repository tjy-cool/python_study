#!/usr/bin/env python
# Funtion:  实现简单的shell sed替换功能
# Filename:
import sys

find_str = sys.argv[1]
repleace_str = sys.argv[2]
filename = 'file'
with open(filename, 'r+', encoding='utf-8') as f:
    for line in f:
        if find_str in line:
            line = line.replace(find_str, repleace_str)
