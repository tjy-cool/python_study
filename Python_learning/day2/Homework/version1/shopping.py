#!/usr/bin/env python
# Funtion:      
# Filename:  shopping.py
#########################################################################################
'''
购物车程序：
1、启动程序后，输入用户名密码后，如果是第一次登录，让用户输入工资，然后打印商品列表
2、允许用户根据商品编号购买商品
3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
4、可随时退出，退出时，打印已购买商品和余额
5、在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示
6、用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买
7、允许查询之前的消费记录
'''
#########################################################################################

_user = 'tom'
_password = 'asdf'
# 1、启动程序后，输入用户名密码后，如果是第一次登录，让用户输入工资，然后打印商品列表
goods = []             # 所有商品列表
login_flag = 0         # 登陆成功标志位，成功为1，不成功为0
while login_flag == 0:        # 没有登陆成功
    username = input('Please input your username: ')
    if username == _user :    # 用户名正确
        password = input('Please input your password: ')
        while password != _password :   # 密码输入不正确
            if password == 'q':         # 输入q, 不想继续试验密码，退出程序
                exit()
            else:                       # 其它则提示输入密码错误，重新输入密码
                print('Password error, please input correct password! ')
                password = input('Please input your password: ')
        else :                          # 输入密码正确，将login_flag置1，表示登陆成功了
            login_flag = 1
    elif username == 'q' :
        exit()
    else :
        print('Username error, please input correct username! ')

# 登陆成功，先读取已购清单文件，如果为空，判断为首次登陆
shopped_goods = []     # 已经消费过的商品清单
# shopped_goods = [['rest_salary',9000],['time',''],[['goods1','money'],['goods2','money']]]
shopped_list_file = open('shopped_list.txt','r+', encoding = 'utf-8' )  # 读写该文件， utf-8格式
if shopped_list_file.read() == '':
    print('Welcome! This is your first time use this software!')
    salary = int(input('Please input your salary: '))
    # shopped_list_file.seek(0)
    shopped_list_file.write('rest_salary,%s'.ljust(30, ' ') % salary)
    shopped_list_file.flush()
else:
    shopped_list_file.seek(0)
    for line in shopped_list_file.readlines():
        val_1 = line.split(',')[0].strip()
        val_2 = line.split(',')[1].strip()
        shopped_goods.append([val_1, val_2])
    # salary = int(shopped_list_file.readline())                   # 读取余额
    print(shopped_goods)
    salary = int(shopped_goods[0][1])

goods_list_file = open('goods_list.txt', 'r', encoding = 'utf-8')        # 只读该文件， utf-8格式
# print('Goods List'.center(50,'-'))              # 打印表头
for line in goods_list_file.readlines():
    goods_name = line.split(',')[0].strip()     # 取出商品名称
    goods_price = int(line.split(',')[1].strip())    # 取出商品价格
    goods.append([goods_name, goods_price])     # 将商品名称和价格保存到goods列表里面
    order_num = int(goods.index([goods_name, goods_price]))  # 该商品的序号
    # print('%d.%s %d' % (order_num, goods_name, goods_price))   # 打印商品列表
# print(60*'-')
goods_list_file.close()         # 关闭文件



# 2、允许用户根据商品编号购买商品
while True:
    print('\033[32;1mGoods List\033[0m'.center(61, '-'))  # 打印表头
    for i in range(len(goods)):
        print('%d.%s %d' % (i, goods[i][0], goods[i][1]))  # 打印商品列表
    print(50 * '-')

    your_choose = input('Please input you want buy goods index: ')
    if your_choose.isnumeric():     # 是纯数字
        your_choose = int(your_choose)
        if your_choose in range(len(goods)):      # 输入商品序号正确
            goods_price = goods[your_choose][1]
            if salary >= goods_price :  # 薪水足够买商品
                salary -= goods_price
                shopped_goods.append([goods[your_choose][0], goods_price])      # 记录已购商品
                shopped_list_file.write('\n%s,%s'% (goods[your_choose][0], goods_price))
                shopped_list_file.flush()
                print('Your rest of money: \033[35;1m%s\033[0m' % salary)  # 打印剩下的工资
            else :  # 不够显示囊中羞涩和剩余薪水
                print('Your cash-strapped now, the rest of your salary is \033[35;1m%s\033[0m.' % salary)
        else :
            print('Your input goods does not exist! Please choose again .')
    elif your_choose == 'q':
        shopped_list_file.seek(0)
        # shopped_list_file.write('rest_salary,%s'.ljust(30,' ') % salary)
        print('Your rest of money: \033[35;1m%s\033[0m' % salary)         # 打印剩下的工资
        print('\033[1;31mYou bought goods list\033[0m'.center(61,'-'))
        for i in range(1,len(shopped_goods)):
            print('%s.%s %s' % (i, shopped_goods[i][0], shopped_goods[i][1]))  # 打印商品列表
        print(50 * '-')
        break
    elif your_choose == 's':
        print('0')
    elif your_choose == 'c':        # 查询
        print('\033[32;1mYour shopped goods list\033[0m'.center(61, '-'))
        for i in range(1, len(shopped_goods)):
            print('\033[1;31m%s. %s %s\033[0m' % (i, shopped_goods[i][0], shopped_goods[i][1]))
        print(50 * '-')
    else:
        print("Your input goods list invalid! Please choose again .")
# 3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
# 4、可随时退出，退出时，打印已购买商品和余额
# 5、在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示
# 6、用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买
# 7、允许查询之前的消费记录

# shopped_list_file.close()       # 关闭文件

# for line in shopped_list_file.readlines():      # 读出已购商品清单
#     shopped_goods[]