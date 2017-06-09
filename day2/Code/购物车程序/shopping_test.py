#!/usr/bin/env python
# Funtion:    购物车程序
# Filename:   shopping_test.py

###############################################
'''
函数功能介绍
购物车程序：
1. 启动程序后，让用户输入工资，然后打印商品列表
2. 允许用户根据商品编号购买商品
3. 用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒 
4. 可随时退出，退出时，打印已购买商品和余额
'''
################################################

f = open('商品.txt','r', encoding='utf-8')

salary = input('Please input your salary: ')
print('The goods are: ')
goods = []
for line in f.readlines():
    goods_name = line.split('. ')[1].strip('\n').split(',')
    goods.append(goods_name)
    print(goods.index(goods_name)+1 , '. ' + goods_name[0] + '\t' + goods_name[1])
# print(goods)

goods_count = len(goods)
choose_goods = []       # 只保存选择的商品编号

while True:
    your_choose = int(input('Please input your choose: '))

    if your_choose-1 in range(goods_count) :
        # if
        choose_goods.append(your_choose)


    else :
        print("Your input goods is does't exit, please input again!")
        continue

