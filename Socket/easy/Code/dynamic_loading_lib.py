#!/usr/bin/env python
# Funtion:      
# Filename:

import importlib
aa = importlib.import_module("lib.aa")
print(aa.CC().name)

lib1 = __import__("lib.aa")
print(lib1)

cc = lib1.aa.CC()
print(cc.name)