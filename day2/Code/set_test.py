#!/usr/bin/env python
# Filename: set.aaa.py

# 创建
list_1 = [1,2,3,4,2,1]
list_1 = set(list_1)

print('1-->',set('2334'))
print('2-->',set(['2','3','4']))
print('3-->',set((1,3,4)))
print('4-->', set({'1':1,'2':2}))

print(list_1, type(list_1))



list_2 = set([1,4,6,34,45,23,45])

# 交集
print(list_1.intersection(list_2))
# 并集
print(list_1.union(list_2))
# 差集
print(list_1.difference(list_2))
print(list_2.difference(list_1))


s = set('a123')
t = set('123t')
# 并集
s.union(t)
s_t = s|t

# 交集
s.intersection(t)
_s_t = s&t

# 差集，当前集合-交集
s.difference(t)
st = s-t

# 对称差集, 并集-交集
s.symmetric_difference(t)
_st = s^t

# 子集，返回True/False
s.issubset(t)
s_in_t = s<=t

# 父集，返回True/False
s.issuperset(t)
s_issuper_t = s >= t

# 长度
len(s)

# 关系测试，in， not in
# '1' in s
print( '1' not in s)