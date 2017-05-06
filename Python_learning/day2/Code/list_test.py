#!/usr/bin/env python
# Filename: list_test.py

# Rat charm, 子鼠
# Ox patient, 丑牛
# Tiger sensitive, 寅虎
# Rabbit articulate, 卯兔
# Dragon healthy, 辰龙
# Snake deep, 巳蛇
# Horse popular, 午马
# Goat elegant, 未羊
# Monkey clever, 申猴
# Rooster deep thinkers, 酉鸡
# Dog loyalty, 戌狗
# Pig chivalrous. 亥猪

# Chinese_Zodiac_Signs = ['Rat', 'Ox', 'Tiger', 'Rabbit']

# print(Chinese_Zodiac_Signs[0])

animals = ['Dog', 'Cat', 'Monkey', 'Chook', 'Snake']
# fish = ['freshwater_fish', 'saltwater_fish']
animals.extend('fish')
print(animals)
animals.sort
# animals.insert(3, 'horse')
# print(animals)

# animals.insert(-4, fish)
# print(animals)
# animals.pop()

# animals.append(fish)
# print(animals)

# animals[3] = 'Horse'
# print(animals)

# animals.append('Ox')
# print(animals)

# animals[0]      # 'Dog'
# animals[3]      # 'Chook'
# animals[-1]     # 'Snake'
# animals[-3]     # 'Monkey'

# animals[1:3]    # ['Cat', 'Monkey']
# animals[3:]     # ['Chook', 'Snake']
# animals[:3]     # ['Dog', 'Cat', 'Monkey']
# animals[:]      # 整个列表
# animals[1:4:2]  # ['Cat', 'Chook']
# animals[::2]    # ['Dog', 'Monkey', 'Snake']

# >>>list_1 = ['x', 'y', 'z', [1, 2, 3]]  # 创建list_1
# >>>list_1_copy = list_1.copy()          # 拷贝list_1
# >>>list_1_copy[1] = 'Y'                 # 修改第一层元素的值
# >>>print(list_1, list_1_copy)           # 修改的位置元素不同
# ['x', 'y', 'z', [1, 2, 3]] ['x', 'Y', 'z', [1, 2, 3]]
# >>>list_1_copy[-1][0] = '123'           # 修改第二层元素的值
# >>>print(list_1, list_1_copy)           # 修改的位置元素相同
# ['x', 'y', 'z', ['123', 2, 3]] ['x', 'Y', 'z', ['123', 2, 3]]

import copy
list_1 = ['x', 'y', 'z', [1, 2, 3]]  # 创建list_1
list_2 = copy.copy(list_1)  # 浅拷贝
list_1[1]= 'Y'
list_2[-1][-3] = '234'
print(list_1, list_2)

import copy
list_1 = ['x', 'y', 'z', [1, 2, 3]]  # 创建list_1
list_3 = copy.deepcopy(list_1)       # 深拷贝
list_1[2]= 'zz'
list_3[-1][-3] = 888
print(list_1, list_3)