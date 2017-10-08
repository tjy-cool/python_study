#!/usr/bin/env python
# Funtion:      
# Filename:

# a = [23,34]
# try :
#     a[2] = 0
# except KeyError as e:
#     print("keyerror")
# except IndexError as e:
#     print("indexerror")

a = "123"
assert type(a) is str
print("assert right")

try :
    assert a == '12'
except AssertionError as e:
    print("change before: ", a)
    a = "12"
    print("after change: ", a)
# b = 12
# assert type(b) is int
# print("b/2 = %s" % (b/2))

