#!/usr/bin/env python
# Filename: three_menu.py
###############################################
# 函数功能介绍
# 三级菜单：
# 1. 运行程序输出第一级菜单
# 2. 选择一级菜单某项，输出二级菜单，同理输出三级菜单
# 3. 菜单数据保存在文件中
# 4. 让用户选择是否要退出
# 5. 有返回上一级菜单的功能
################################################

# 读取文件保存到字典中，注意去掉第一行网址
# 需要保存的样板
# dict = {'北京市':          # count = 0
#             {'985':['清华大学','北京大学'],     # count = 1
#              '211':['北京交通大学']},          # count = 2
#         '天津市':
#             {'985': ['南开大学', '天津大学'],
#              '211': ['天津医科大学']}
#         }

dict_university = {}    # 所有数据
# dict_level = {}         # key为'985'或'211'， value为大学
f = open('province-985_211-university.txt', 'r', encoding='utf-8')
# print(f)
count = 0   # 目前是省份级
for uni in f.readlines():
    # print(uni)
    if uni == '\n' or uni.startswith('http'):   # 跳过 空行和网址
        continue
    elif uni.split('.')[0].isnumeric():       # 当前行 为省份名称
        count = 0                             # 计数器
        province = uni.split('.')[1].strip()
        dict_university[province] = {}
    elif uni.strip().isnumeric() :             # 985 或 211
        level = uni.strip()
        if level == '985':
            dict_university[province][level] = []       # 985学校，key
            # dict_level[level] = []
            count = 1
        if level == '211':
            dict_university[province][level] = []       # 211学校,key
            # dict_level[level] = []
            count = 2
    elif '、' in uni.strip() and count == 1:             # 985 学校名称,以顿号（、）结尾, value
        university = uni.strip().split('、')
        dict_university[province][level].extend(university)
    elif '\t' in uni.strip() and count == 1:            # 985 学校名称,以制表符（\t）结尾, value
        university = uni.strip().split('\t')
        dict_university[province][level].extend(university)
        # dict_level[level].extend(uni.strip().split(','))
    elif '、' in uni.strip() and count == 2:           # 211学校名称,以顿号（、）结尾,即value
        university = uni.strip().split('、')
        dict_university[province][level].extend(university)
    else :                                             # 211学校名称,以制表符（、）结尾,即value
        university = uni.strip().split('\t')
        dict_university[province][level].extend(university)
        # dict_level[level].extend(uni.strip().split(','))

f.close()
# print(dict_university)

# 显示程序功能提示信息：
print('此程序拥有以下功能'.center(50,'-'))
print('\t1.查询各个省份的985学校和211学校'.expandtabs(tabsize=10))
print('\t2.进入下一层直接输入下一层的名称'.expandtabs(tabsize=10))
print('\t3.返回上一层请直接按(b)'.expandtabs(tabsize=10))
print('\t4.返回首层请直接按(b1)'.expandtabs(tabsize=10))
print('\t5.退出请直接按(q)'.expandtabs(tabsize=10))
print(''.ljust(59,'-'))

# 1. 运行程序输出第一级菜单
print(list(dict_university.keys()))
# for key in dict_university:   # 此时打印为纵列，不利于观察
#     print(key, end = ' ')


level_cnt = 1   # 目前在1级，将用户所在的位置作为第几级
while True:
    # 根据在不同菜单下输出不同的提示信息
    if level_cnt == 1:
        operate = input('请输入您需要查询的省份名称：')
    elif level_cnt == 2:
        operate = input('请输入您需要查询的该省的某一等级的学校数量（985/211）：')
    else:
        operate = input('返回上一级请按(b),返回第一级请按(b1),退出请按(q):')
    # 2. 选择一级菜单某项，输出二级菜单，同理输出三级菜单
    if level_cnt == 1 and operate not in ['b', 'q']:
        if operate in dict_university:
            province = operate     # 记录进入的省份
            print(list(dict_university[operate].keys()))
            level_cnt = 2
            continue
        else:
            print('输入省份出错,请重新输入!')
    if level_cnt == 2 and operate not in ['b', 'q']:
        if operate in dict_university[province]:
            level = operate
            level_list = dict_university[province][level]
            print(level_list)
            level_cnt = 3
            continue
        else:
            print('学校分区输入错误,请重新输入!')
    if level_cnt == 3 and operate == 'b1':
        print(list(dict_university.keys()))
        level_cnt = 1
        continue
    # 3. 菜单数据保存在文件中
    # 4. 让用户选择是否要退出
    if operate == 'q':
        exit_flag = input('确定要退出，不退出请按(n),否则任意按某一按键:')
        if(exit_flag == 'n'):
            continue
        else:
            break
    # 5. 有返回上一级菜单的功能
    if operate == 'b':
        if level_cnt == 2 :
            print(list(dict_university.keys()))
            level_cnt = 1
        elif level_cnt == 3 :
            print(list(dict_university[province].keys()))
            level_cnt = 2
        else :
            print('没有该省份，请重新输入')
            continue
