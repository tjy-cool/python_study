# 创建空字典，常定义在循环之前
dict1 = {}
# # 创建普通字典
# stu_grade = {'stu1001': 95, 'stu1002': 80, 'stu1003': 75}
# 创建嵌套字典
stu_info = { 'stu1001': {'name': 'Jack', 'gender': 'male', 'age': 26},
            'stu1002': {'name': 'Tom', 'gender': 'male', 'age': 25}, 
            'stu1003': {'name': 'Lucy', 'gender': 'female', 'age': 25}}

# 字典工厂dict函数方法
dict2 = dict((('name','Jack'), ['gender','male'], ['age', 26]))
print(dict2)

# 内建fromkeys()方法，第一个参数为不能为集合类型，第二个参数为可以数据类型
dict_1 = {}.fromkeys('xyz', 100)
dict_2 = dict.fromkeys(['x', 'y', 'z'], [12,23])
dict_3 = {}.fromkeys(('x', 'y', 'z'), '234')
dict_4 = dict.fromkeys({'age':20, 'gender': 'male'},100)    # 注意此时的结果
dict_5 = dict.fromkeys('xyz')
print(dict_1)   # {'y': 100, 'z': 100, 'x': 100}
print(dict_2)   # {'y': [12, 23], 'z': [12, 23], 'x': [12, 23]}
print(dict_3)   # {'y': '234', 'z': '234', 'x': '234'}
print(dict_4)   # {'gender': 100, 'age': 100}
print(dict_5)   #  {'y': None, 'z': None, 'x': None}

# 修改元素
dict_1['x'] = 200
dict_2['x'][0] = 34
dict_1['w'] = 1000
dict_2['w'] = [100, 100]
dict_2['w'][0] = 99
print(''.center(50,'-'))
print(dict_1)
print(dict_2)
# 创建普通字典
stu_grade = {'stu1001': 95, 'stu1002': 80, 'stu1003': 75}
# 增加元素
stu_grade['stu1004'] = 100
# 修改元素
stu_grade['stu1004'] = 89
# 删除元素  pop方法，del删除，popitem随机删除方法

# 查找
# in 标准查找方法,存在返回True，否则返回False
print('stu1001' in stu_grade)
# 获取 get方法,没有找到返回 None ,否则返回正确的值
print(None == stu_grade.get('stu1005'))
#类下标法，存在返回value, 不存在出错，使用请注意
print(stu_grade['stu1003'])      # 75
# print(stu_grade['stu1005'])       #出错
#
# print(stu_grade.values())
# print(type(stu_grade.values()))
# print(stu_grade.keys())
# print(type(stu_grade.keys()))

# setdefault方法，如果该 key - value 存在，则不变，否则增加成员, 并且返回真正的value
# stu_grade.setdefault('stu1006', 98)   # {'stu1001': 95, 'stu1006': 98, 'stu1004': 89, 'stu1002': 80, 'stu1003': 75}
# bb.txt = stu_grade.setdefault('stu1003', 98)     # {'stu1004': 89, 'stu1003': 75, 'stu1002': 80, 'stu1001': 95}
# print(stu_grade)
# print(bb.txt)
#
# print('----------')
# print(enumerate(stu_grade))     # 得到地址
#
# # dict.items
# print(stu_grade.items())
#
# for key in stu_grade:
#     print(key)
#
# for key, value in stu_grade.items():    # 需要先转换为列表，然后取出key和value，
#     print('%s: %s' %(key, value))
#
# for index, key in enumerate(stu_grade):
#     print('%s: %s' % (index, key))

# a.update(b)方法，相当于 复制+替换

#
# print('---------')
# print(dict_1)
#
# # 增加元素
# stu_info['stu1004'] = {'name': 'Katty', 'gender': 'famale', 'age': 24}
# stu_grade['stu1004'] = 90
# # 修改元素
# stu_info['stu1001']['age'] = 27
# stu_grade['stu1001'] = 89
#
# # 删除元素，方法有pop(), del, popitem()
# # stu_info.pop('stu1004')         # pop 方法
# # stu_grade.pop('stu1004')
#
# # del stu_info['stu1004']
# # del stu_grade['stu1004']
#
# # stu_info.popitem()      # popitem()方法  随机删
# # stu_grade.popitem()
#
# print(stu_info)
# print(stu_grade)
#
#
#
# dict1 = { '2':2, '1':23, '1':24, '1':[123, 23]}
# print(dict1)