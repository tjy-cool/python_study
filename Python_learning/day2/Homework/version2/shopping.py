#!/usr/bin/env python
# Funtion:      
# Filename:
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

import time, sys
__version__ = '0.0.2'

def welcome():
    '''登陆欢迎信息'''
    for i in range(6) :
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.2)
    print("\nwelcome! you are login...")  # 相等打印欢迎信息

def file_2_dict(file_handle, split_str = ','):
    '''
    文件转换为字典，
    :param file_handle: 文件句柄
    :param dict: 字典
    :param split_str: 
    :return: 
    '''
    dict_1 = {}
    file_handle.seek(0)
    for line in file_handle.readlines():
        key_1 = line.split(split_str)[0].strip()
        val_1 = line.split(split_str)[1].strip()
        dict_1[key_1] = val_1
    return dict_1

def file_2_list(file_handle, split_str=','):
    '''
    文件内容保存为二级列表
    :param file_handle: 文件句柄
    :param split_str: 分割符
    :return: 二级列表
    '''
    list = []
    file_handle.seek(0)
    for line in file_handle.readlines():
        val_1 = line.split(split_str)[0].strip()
        val_2 = line.split(split_str)[1].strip()
        list.append([val_1,val_2])
    return list

def login(user_file, err_file):
    '''
    用户登陆
    :param user_file: 用户密码保存文件
    :param err_file: 错误登陆保存文件
    :return: user用户名
    '''
    user_file = open(user_file, 'a+', encoding='utf-8')     # 打开文件
    err_file = open(err_file, 'a+', encoding='utf-8')
    username_passwd = file_2_dict(user_file)  # 用户名密码
    err_info_dict = file_2_dict(err_file,':') # 错误登陆
    max_try_cnt,try_cnt = 3,0                # 运行最大尝试次数
    # out_user = ''
    user = input('Please input your username: ')
    if user in username_passwd.keys():  # 判断用户名是否在username_passwd字典的key里面
        if user in err_info_dict.keys():  # 若用户名在错误信息文本中，则已经被锁定了
            print("you have been locked at time :", err_info_dict[user])
            exit()
        else:  # 用户名不在错误信息文本中，则可以正常输入和登陆
            while  try_cnt < max_try_cnt:
                password = input('Please input your password: ')
                if username_passwd[user] == password:  # 认证成功后欢迎信息 ,判断密码是否与真实密码相等
                    welcome()
                    # out_user = user
                    break  # 退出循环
                elif password == 'q':    # 取消重新登陆，直接退出程序
                    exit()
                else:   # 未达到三次，最大尝试次数减一
                    try_cnt += 1
                print('You have %s times chance' % (max_try_cnt-try_cnt))
            else:  # 输入三次错误后锁定
                localTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if err_info_dict == {}:
                    err_file.write('%s:%s' %(user,localTime))
                else:
                    err_file.write("\n%s:%s" %(user, localTime))
                print("you have been locked...")
                exit()
    else:
        save_user = input("Do you want add a new user (y/n)? ")
        if (save_user == 'y'):
            cur_passwd = input('Please input a passwd for the new user:')
            username_passwd[user] = cur_passwd
            user_file.write('\n%s,%s' %(user, cur_passwd))
            # out_user = user
        else:
            exit()
    user_file.close()
    err_file.close()
    return user

def show_list(list_tittle, list):
    '''
    显示二级列表
    :param list_tittle: 顶部名称
    :param list: 二级表格
    :return: 
    '''
    print(('\033[32;1m%s\033[0m' % list_tittle).center(61, '-'))
    print('\033[1;31mOrder'.center(15,' ') + '|' +
          'Goods'.center(28,' ') + '|' +
          'Price\033[0m'.center(18,' '))

    for i in range(0, len(list)):
        print(('\033[1;31m%s' % i).center(15, ' ') + '|' +
              ('%s' % list[i][0]).center(28, ' ') + '|' +
              ('%s\033[0m' % list[i][1]).center(18, ' '))
        # print('\033[1;31m%s. %s %s\033[0m' % (i, list[i][0], list[i][1]))
    print(50 * '-')

def acquire_salary(user):
    '''
    确定用户的当前薪水，
    如果该用户没有对应的已购买清单文件，
    则提示输入薪水并新建以user_bought.txt为名称的清单文件，
    如果该用户有对应的已购清单文件，则读取剩余薪水
    :param user: 
    :return: 
    '''
    bought_file = user+'_bought.txt'
    # f = open(bought_file, 'a+', encoding='utf-8')
    with open(bought_file, 'a+', encoding='utf-8') as f:
        f.seek(0)
        if f.readline() == '':
            print('This is your first time use this software!')
            salary = int(input('Please input your salary: '))
            f.write('rest_salary,%s'.ljust(30, ' ') % salary)
            f.flush()
        else :
            f.seek(0)
            line1 = f.readline()
            salary = int(line1.split(',')[-1].strip())
            print('Your rest of money: \033[35;1m%s\033[0m' % salary)  # 打印剩下的工资
    # f.close()
    return bought_file,salary

def shopping(boughtfile_salary, bought_file, goods_list_file):
    bought_file = boughtfile_salary[0]
    salary = boughtfile_salary[1]
    bought_file_handle = open(bought_file, 'r+', encoding='utf-8')
    bought_file_handle.readline()
    bought_goods = file_2_list(bought_file_handle, ',')
    this_time_bought_goods_list = []
    with open(goods_list_file, 'r', encoding='utf_8') as f:
        goods_list = file_2_list(f)
    show_goods_flag = 1
    while True:
        if show_goods_flag:
            show_list('Goods List',goods_list)
        your_choose = input('Please input you want buy goods index: ')
        if your_choose.isnumeric():   # 为纯数字
            your_choose = int(your_choose)
            if your_choose in range(len(goods_list)):
                goods_price = int(goods_list[your_choose][1])
                if salary >= goods_price:
                    salary -= goods_price
                    goods_name = goods_list[your_choose][0]
                    this_time_bought_goods_list.append([goods_name,goods_price])
                    bought_file_handle.write('\n%s,%s'%(goods_name, goods_price))
                    bought_file_handle.flush()
                    print('Your rest of money: \033[35;1m%s\033[0m' % salary)  # 打印剩下的工资
                    print('\033[1;31;44m%s\033[0m have been added to the bin_shopping cart!'% goods_name)
                    show_goods_flag = 1
                else:  # 不够显示囊中羞涩和剩余薪水
                    print('Your cash-strapped now, the rest of your salary is '
                          '\033[35;1m%s\033[0m.' % salary)
                    show_goods_flag = 0
            else:
                print("Your choose goods not exist! Please choose again .")
        elif your_choose == 'q':    # quit 推出
            bought_file_handle.seek(0)
            bought_file_handle.write('rest_salary,%s'.ljust(30, ' ') % salary)
            show_list('You bought goods list', this_time_bought_goods_list)
            print('Your rest of money: \033[35;1m%s\033[0m' % salary)  # 打印剩下的工资
            show_goods_flag = 0
            break
        elif your_choose == 'c' :   # check 查询
            show_list('This time You bought goods list', this_time_bought_goods_list)
            show_list('Before this time You bought goods list', bought_goods)
            show_goods_flag = 0
        else :
            print("Your input goods list invalid! Please choose again .")
    bought_file_handle.close()


user = login('username_passwd.txt', 'err.txt')
if user != '':  # 成功登陆
    boughtfile_salary = acquire_salary(user)
    shopping(boughtfile_salary, 'bought_goods.txt', 'goods_list.txt')
else:           # 没有成功登陆
    print('login err!')

