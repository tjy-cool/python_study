#!/usr/bin/env python
# Funtion:      
# Filename:
import time
from core import data_handler
from core import transaction
from core import login
from core import logger

#temp account data ,only saves the data in memory
user_data = {
    'account_id':None,
    'is_authenticated':False,
    'account_data':None
}

def account_info(acc_data):
    '''
    查询账户信息
    :param acc_data: 
    :return: 
    '''
    account_data = data_handler.get_user_db(acc_data['account_id'])
    log_obj = logger.logger(account_data['id'], 'access')
    info_title = ("\033[31;m %s's Bank info\033[0m" % acc_data['account_id']).center(55, '-')
    info_body = '''\033[32;m
    username:           %s
    credit:             %s
    balance:            %s
    enroll date:        %s
    expire date:        %s
    last logout data:   %s
\033[0m''' % (account_data['id'], account_data['credit'],
              account_data['balance'], account_data['enroll_date'],
              account_data['expire_date'], account_data['last_login_time'])

    info = info_title + info_body + '-'*45
    print(info,flush=True)
    log_obj.info('account [%s] query the account information' % account_data['id'])


def repay(acc_data):
    '''
    还款
    :param acc_data:   包含user_db和用户是否登陆 的字典
    :return: 
    '''
    account_data = data_handler.get_user_db(acc_data['account_id'])
    log_obj = logger.logger(account_data['id'], 'transaction')
    current_balance = '''---------------- BALABCE INFO --------------
            Credit :  %s
            Balance:  %s
    -------------------------------------------''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        repay_amount = input('\033[1;34mInput repay amount: \033[0m').strip()
        if len(repay_amount)>0 and repay_amount.isdigit():
            new_balance = transaction.make_transaction(log_obj, account_data, 'repay', repay_amount)
            if new_balance:
                print('New:Balance:\033[32;1m %s \033[0m' % new_balance['balance'] )
        elif repay_amount == 'b':   # 返回
            back_flag = True
        elif repay_amount == 'q':   # 退出程序
            exit('请保管好您的信用卡，欢迎下次使用！')
        else:   # 错误输入
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % repay_amount)



def withdraw(acc_data):
    '''
    提现
    :param acc_data: 
    :return: 
    '''
    account_data = data_handler.get_user_db(acc_data['account_id'])
    log_obj = logger.logger(account_data['id'], 'transaction')
    current_balance = '''---------------- BALABCE INFO --------------
            Credit :  %s
            Balance:  %s
-------------------------------------------''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        withdraw_amount = input('\033[1;34mInput withdraw amount: \033[0m').strip()
        if withdraw_amount.isdigit():
            new_balance = transaction.make_transaction(log_obj, account_data, 'withdraw', withdraw_amount)
            if new_balance:
                print('New:Balance:\033[32;1m %s \033[0m' % new_balance['balance'])
        elif withdraw_amount == 'b':   # 返回
            back_flag = True
        elif withdraw_amount == 'q':   # 退出程序
            exit('请保管好您的信用卡，欢迎下次使用！')
        else:   # 错误输入
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % withdraw_amount)

def transfer(acc_data):
    '''
    转账
    :param acc_data: 
    :return: 
    '''
    account_data = data_handler.get_user_db(acc_data['account_id'])
    log_obj = logger.logger(account_data['id'], 'transaction')
    all_user = data_handler.get_all_username()  # 存在data/accounts文件夹下的所有用户
    current_balance = '''---------------- BALABCE INFO --------------
                Credit :  %s
                Balance:  %s
-------------------------------------------''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        tran_id = input('\033[1;34mInput what account you want transfer: \033[0m').strip()
        if tran_id in all_user: # 用户存在
            tran_amount = input('\033[1;34mInput withdraw amount: \033[0m').strip()
            if tran_amount.isdigit():   # 数字
                new_balance = transaction.make_transaction(log_obj, account_data, 'withdraw', tran_amount)
                if new_balance: # 返回的 new_balance 有效，即钱够
                    # 汇款方进行相关操作并进行相关日志记录
                    tran_data = data_handler.get_user_db(tran_id)
                    tran_data['balance'] += int(tran_amount)
                    data_handler.set_user_db(tran_id,tran_data)
                    traned_log_obj = logger.logger(tran_id, 'transaction')
                    traned_log_obj.info('Received account %s transfer amount %s' % (account_data['id'], tran_amount))

                    print('New:Balance:\033[32;1m %s \033[0m' % new_balance['balance'])
            elif tran_amount == 'b':  # 返回
                back_flag = True
            elif tran_amount == 'q':  # 退出程序
                exit('请保管好您的信用卡，欢迎下次使用！')
            else:  # 错误输入
                print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % tran_amount)
        elif tran_id == 'b':  # 返回
            back_flag = True
        elif tran_id == 'q':  # 退出程序
            exit('请保管好您的信用卡，欢迎下次使用！')
        else:  # 错误输入
            print('\033[31;1m[%s] is not a valid id' % tran_id)


# 账单
def pay_check(acc_data):

    pass

# 退出登陆
def logout(acc_data):
    pass

def interactive(acc_data):
    menu_title = "\033[31;m Bank Action Menu \033[0m".center(55, '-')
    # menu_title = ("\033[31;m %s's Bank Action Menu \033[0m" % acc_data['account_id']).center(55, '-')
    menu_body = '''\033[32;1m
    1. 账户信息     2. 还款       3. 取款
    4. 转账         5. 账单       6. 退出\033[0m
'''
    menu = menu_title + menu_body + '-' * 44
    menu_dict = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': logout
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input('>> ').strip()
        if user_option in menu_dict:
            # print('accdata ',acc_data)
            menu_dict[user_option](acc_data)
        elif user_option == 'q':
            exit()
        else:
            print("\033[31;1mOption does not exist!\033[0m")

def run():
    user_db = login.acc_login(user_data)
    # print(user_db)
    if user_data['is_authenticated']:
        user_data['account_data'] = user_db
        interactive(user_data)