#!/usr/bin/env python
# Funtion:      
# Filename:
#########################################################################################
'''
1. 根据用户输入输出对应的backend下的server信息
2. 可添加backend 和sever信息  a
3. 可修改backend 和sever信息  m
4. 可删除backend 和sever信息  d
5. 操作配置文件前进行备份      HAproxy_back.txt
6 添加server信息时，如果ip已经存在则修改;如果backend不存在则创建；若信息与已有信息重复则不操作
配置文件 参考 http://www.cnblogs.com/alex3714/articles/5717620.html
'''
#########################################################################################

def input_2_dict(cnt = 8):
    '''
    将输入的字典格式的字符串 转换为 程序中的字典
    输入格式如下：
    """
    {
        'bakend': 'www.oldboy.org',
        'record':{
            'server': '100.1.7.9',
            'weight': 20,
            'maxconn': 30
        }
    }
    """
    :param cnt: 字符串格式的字典的有效行数
    :return:    转换后的字典
    '''
    input('Please input a dict of backend and server:')
    str = ''
    for i in range(cnt):
        str += input().strip()
    str2dict = eval(str)
    input()
    return str2dict

def input_2_format_dict():
    input_dict = input_2_dict()
    format_dict = {}
    format_dict['backend'] = input_dict['backend']
    format_record = input_dict['record']
    format_record['server'] = [input_dict['record']['server']]
    format_dict['record'] = [format_record]
    return format_dict

def show_function_info():
    ''' 在程序运行开始时，显示程序的功能 '''
    print(('\033[32;1m%s\033[0m' % '程序功能如下').center(56,'-'))
    print('\033[31;1m',end='')
    print('\t命令：a  添加backend 和sever信息 '.expandtabs(5))
    print('\t命令：m  修改backend 和sever信息 '.expandtabs(5))
    print('\t命令：d  删除backend 和sever信息 '.expandtabs(5))
    print('\t命令：c  查询backend的记录'.expandtabs(5))
    print('\t命令：q  退出程序的'.expandtabs(5))
    print('\033[0m',end='')
    print(50*'-')

def backup(file_name):
    str = ''
    with open(file_name, 'r', encoding='utf-8') as f, \
            open(file_name+'.back', 'w+', encoding='utf-8') as  f_back:
        f_back.write(f.read())

def add_modify_backend(input_format_dict, backend_list):
    '''
    将add_dict加入到backend_list中
    :param input_format_dict: 输入的backend字典
    :param backend_list: 该列表中保存了所有的 以字典形式保存的backend
    :return: 返回增加/修改了新的backend 的所有字典组成 的列表
    '''
    input_backend = input_format_dict['backend']
    input_record_list = input_format_dict['record']
    # input_server = input_record_list[0]['server']
    input_weight = input_record_list[0]['weight']
    input_maxconn = input_record_list[0]['maxconn']
    same_backend_flag = 0
    for backend_dict in backend_list:
        if input_backend == backend_dict['backend']:    # 存在相同的website
            same_backend_flag = 1
            # print(input_backend, backend_dict['backend'])
            record_list = backend_dict['record']
            find_flag = ip_in_record_list(input_record_list[0], record_list)
            if find_flag == -2 :  # 不存在相同的website
                backend_list[backend_list.index(backend_dict)]['record'].extend(input_record_list)
                print('\033[35;1mAdd new record at the backend of %s \033[0m'
                      % backend_list[backend_list.index(backend_dict)]['backend'])
            elif find_flag == -1:   # server行相同
                print('\033[35;1mHas the same backend, Do Nothing！\033[0m')
            else :  # ip地址不同，增加一条server行
                record_list[find_flag]['weight'] = input_weight
                record_list[find_flag]['maxconn'] = input_maxconn
                print('\033[35;1mHas same IP, just update!\033[0m')
    if same_backend_flag == 0:      # ip地址相同, 但是weight和maxconn不同，只更新weight和maxconn
        backend_list.append(input_format_dict)
        print('\033[35;1mAdd the new backend successful!\033[0m')

    return backend_list

def ip_in_record_list(one_record_dict, record_list):
    '''
    
    :param one_record_dict: 
    :param record_list: 
    :return: 
    '''
    ip = one_record_dict['server'][0]
    weight = one_record_dict['weight']
    maxconn = one_record_dict['maxconn']
    find_ip_flag = -2  # -2为没有找到IP, -1为找到的一行相同的server行， 1-n 为找到相同ip对应的下标
    for index, record_dict in enumerate(record_list):
        for server_ip in record_dict['server']:
            if server_ip == ip:
                find_ip_flag = index
                if weight == record_dict['weight'] and maxconn == record_dict['maxconn']:
                    find_ip_flag = -1
    return find_ip_flag

def del_backend(input_format_dict, backend_list):
    input_backend = input_format_dict['backend']
    input_record_list = input_format_dict['record']
    for backend_dict in backend_list:
        if input_backend == backend_dict['backend']:
            record_list = backend_dict['record']
            find_flag = ip_in_record_list(input_record_list[0], record_list)
            print('\033[35;1m')
            if find_flag == -1:
                backend_list[backend_list.index(backend_dict)]['record'].remove(input_record_list[0])
                if backend_list[backend_list.index(backend_dict)]['record'] == []:  #当前backend下没有record
                    del backend_list[backend_list.index(backend_dict)]
                print('Success del the backend!')
            else :
                print('Has the same backend, but has no same record')
            print('\033[0m')
    return backend_list

def query_backend(input_website,backend_list):
    find_success_flag = -1
    for index, backend_dict in enumerate(backend_list):
        if input_website == backend_dict['backend']:
            find_success_flag = index
    if find_success_flag == -1:
        print('\033[35;1mUnfound the backend!\033[0m')
    else:
        return backend_list[find_success_flag]

def write_all_str(file_name, format_backend_list, start_str = ''):
    '''
    写整篇文档的数据
    :param file_name: 文件名
    :param start_str: 开始部分的信息，即第一个backend的信息前的所有字符串
    :param backend_list: 所有backend组成的列表
    :return: 
    '''
    for format_backend_dict in format_backend_list:  # 将backend格式化的字符串 追加加到 开始字符串上面
        start_str += format_backend_dict_2_format_str(format_backend_dict)
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(start_str)

def format_backend_dict_2_format_str(backend_dict,*args):
    '''
    将backend字典保存到格式化的字符串
    :param dict: 需要保存的字典
    :param args: 字典的key，无设置为('backend','record', 'server', 'weight', 'maxconn')
    :return: 返回输出的格式化的字符串
    '''
    if args == ():
        args = ('backend','record', 'server', 'weight', 'maxconn')
    backend_str = '%s %s\n' % (args[0], backend_dict[args[0]])
    record_list = backend_dict[args[1]]
    for record_dict in record_list:
        server_str = args[2]   # server_str 为以server开始的行
        server_list = record_dict[server_str]   # server_list为server中含IP的个数
        server_str += ' '
        for ip in server_list :
            server_str += ip
            server_str += ' '
        weight_str = '%s %s ' % (args[3], record_dict[args[3]])
        maxconn_str = '%s %s\n' % (args[4], record_dict[args[4]])
        server_str += weight_str
        server_str += maxconn_str

        server_start_str = '\t'.expandtabs(8)  # record
        backend_str += server_start_str + server_str
    return backend_str + '\n'

def read_txt(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        start_str = ''
        format_backend_list = []
        backend_appear_cnt = -1
        for line in f:
            if line.startswith('backend'):
                backend_appear_cnt += 1
                format_backend_list.append({})
            if backend_appear_cnt == -1: # 出现backend之前
                start_str += line
            else:   # 已经出现以backend开始的行了
                if 'backend' in line:
                    format_backend_list[backend_appear_cnt]['backend'] = line.split(' ')[1].strip()
                    format_backend_list[backend_appear_cnt]['record'] = []

                elif 'server' in line:  # 非空行
                    list1 = line.strip().split(' ')
                    weight_index = list1.index('weight')

                    format_server_dict = {}
                    format_server_dict['server'] = list1[1:weight_index]
                    format_server_dict['weight'] = int(list1[-3].strip())
                    format_server_dict['maxconn'] = int(list1[-1].strip())
                    # format_record_list.append(format_server_dict)
                    format_backend_list[backend_appear_cnt]['record'].append(format_server_dict)
                    # print(format_backend_list)
                else :              # 空行,结束backend的范围

                    # format_backend_list.append(format_backend_dict)
                    continue


                # format_backend_list[backend_appear_cnt] = {}
    return start_str, format_backend_list

def main():
    file_name = 'HAproxy.txt'
    tuple1 = read_txt(file_name)
    start_str = tuple1[0]
    backend_list = tuple1[1]
    while True:
        show_function_info()  # 显示功能信息
        your_choose = input('Please input your choose: ')
        if your_choose in ('a','d','m') :   # 增加、修改和删除
            input_format_dict = input_2_format_dict()      # 提示输入字符串形式的字典
            backup(file_name)               # 备份文件
            if your_choose in ('a', 'm'):   # 增加或修改
                backend_list = add_modify_backend(input_format_dict,
                                                  backend_list)  # 将增加的元素添加到列表
            else:
                del_backend(input_format_dict, backend_list)
            write_all_str(file_name, backend_list, start_str)  # 将更新的列表写入到文件中
        elif your_choose == 'c':        # 查询
            input_website = input('Please input the website what you want looking for:')
            res = query_backend(input_website, backend_list)
            if res != None:     # 没有查询到
                out_str = format_backend_dict_2_format_str(res)
                print(out_str)
        elif your_choose == 'q':  # 退出
            exit()
        else :   # 错误输入
            print('Input error! no operation for that! ')

if __name__ == '__main__':
    main()

