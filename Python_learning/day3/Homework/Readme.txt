本程序实现的功能有：
1. 命令详解
-------------------程序功能如下--------------------
     命令：a  添加backend 和sever信息
     命令：m  修改backend 和sever信息
     命令：d  删除backend 和sever信息
     命令：c  查询backend的记录
     命令：q  退出程序的
--------------------------------------------------
2. 原始文件为：HAproxy.txt
   备份文件为：HAproxy.txt.back
   每次操作之前都会进行备份，如进行增加，删除和修改操作前会进行文件备份

3. 本程序努力把函数之间的耦合性降为最低，
    采用了类似于分层的思想，主要分为以下几层：
    用户接口层： 用于提醒用户输入和接收用户的输入数据，
                函数有：input_2_dict()， input_2_format_dict(), show_function_info()
    文件操作层： 直接与文件接触，
                函数有：read_txt(), write_all_str(), backup()
    命令处理层：主要用户对用户输入的命令进行相应处理，
                函数有：add_modify_backend()， del_backend()， query_backend(),
    数据处理层：主要对数据进行处理的一些中间程序，相当于底层的处理函数
                函数有：ip_in_record_list

4. 输入backend的标准格式为：
"""
{
    'backend': 'www.oldboy.org',
    'record':{
        'server': '220.2.8.10',
        'weight': 20,
        'maxconn': 30
    }
}
"""

5. 查询时输入的标准格式为：
www.hao123.com
