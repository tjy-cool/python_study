#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Wang SiNing

file_list = []           #用来存储配置文件
file_list_new = []        #用来存储配置文件backend之前的文件内容
backend_dict = {}         #用来存储backend与server的信息

def reread():
    "将文件内容追加到file_list列表"
    with open("HAproxy.conf", "r", encoding="utf-8") as f:  # 打开文件并赋值给句柄f
        for i in f:
            file_list.append(i.rstrip())  # 将打开的文件以列表的方式存储并追加到列表file_list


def show_html():
    "显示文件中存在多少包含backend的行"
    # print(backend_dict)
    print("当前文件中存在的网址：")
    for i in backend_dict:                #打印文件中所有的backend的网址信息
            print(i)

def write_file():
    "将文件备份并将字典中的内容追加到backend之前的列表并写入到文件"
    f = open("HAproxy.conf","w",encoding="utf-8")               #打开配置文件
    f1 = open("HAproxy.conf.bak","w",encoding="utf-8")          #打开配置文件的备份分文件
    for i in file_list:                                             #将备份文件逐行写入到备份文件中
        f1.write(str(i)+"\n")
    f1.close()
    for i in backend_dict:                                         #将backend_list按指定的格式追加到file_list_new中
        file_list_new.append("backend %s"%i)
        for j in backend_dict[i]:
            file_list_new.append("        server %s weight %s maxconn %s"%(backend_dict[i][j]["server"],backend_dict[i][j]["weight"],backend_dict[i][j]["maxconn"]))
        file_list_new.append("")
    for i in file_list_new:                                 #将file_list_new的内容逐行写入到配置文件中
        f.write(str(i)+"\n")
    f.flush()
    f.close()



def find_backend():
    "查找到文件中的backend网址和对应的server信息并赋值到一个字典"
    backend_index = 0              # backend所在的索引
    backend_index_list = []           # backend所在索引组成的列表
    for index,i in enumerate(file_list):
        k1 = str(i).strip().split(" ")                  #将文件中的行的左右的空格删除并将行的内容用空格分开生成列表
        if k1[0] == "backend":                        #如果行生成的列表第一个元素是backend，说明行首为backend
            backend_index_list.append(index)           # 将此时对应的索引追加到back_index_list
            backend_index = index                      # 并将backend_index设置为当前的索引的值
        elif k1[0] == "backend" and backend_index < index:
            backend_index_list.append(index)
    file_list_new.extend(file_list[:backend_index_list[0]])       #将文件开头到第一个backend的行放入到file_list_new中
    length_backend_index = len(backend_index_list)
    for j in range(length_backend_index):
        if length_backend_index == 1 or j == length_backend_index - 1:    #这句说明文件中不含backend或者就有一个backend
            end_backend = None
        else:
            end_backend = backend_index_list[j+1] - 1
        k2 = str(file_list[backend_index_list[j]]).strip().split(" ")
        backend_dict[k2[1]] = {}
        file_list_server = file_list[backend_index_list[j]+1:end_backend]
        while "" in file_list_server:                    #去除backend信息之间所有的空格
            file_list_server.remove("")
        for index1,k in enumerate(file_list_server):               # 将两个backend之间的所有列表元素添加到字典中
            k3 = k.strip().split(" ")
            backend_dict[k2[1]][index1] ={"server":k3[1],"weight":k3[3],"maxconn":k3[5]}


def select_html():
    "查看输入网址对应的信息"
    wangzhi = input("请输入需要查询的网址:")
    if wangzhi in backend_dict:
        for i in backend_dict[wangzhi]:                   #如果网址在back_dict中，将对应的信息按指定的格式显示出来
            server = backend_dict[wangzhi][i]["server"]
            weight = backend_dict[wangzhi][i]["weight"]
            maxconn = backend_dict[wangzhi][i]["maxconn"]
            print("server %s weight %s maxconn %s" %(server,weight,maxconn))
    else:
        print("查询的网址不存在！")

def add_html():
    "增加输入网址对应的信息"
    flag = 0
    next_record = 0
    wangzhi_dict = eval(input("请输入需要增加的网址信息:(例如:{'backend': 'www.oldboy.org','record':{'server': '100.1.7.9','weight': 20,'maxconn': 30}})"))
    if wangzhi_dict["backend"] in backend_dict:                         # 网址在back_dict中
        for i in backend_dict[wangzhi_dict["backend"]].keys():
            if backend_dict[wangzhi_dict["backend"]][i]["server"] == wangzhi_dict["record"]["server"]:           # 如果增加的网址的server在back_dict中，就修改对应的server信息
                backend_dict[wangzhi_dict["backend"]][i]["weight"] = str(wangzhi_dict["record"]["weight"])
                backend_dict[wangzhi_dict["backend"]][i]["maxconn"] = str(wangzhi_dict["record"]["maxconn"])
                flag += 1
            next_record += 1
        if flag == 0:                    #如果增加的网址的server不存在back_dict中，就添加server和server信息到back_dict中
            backend_dict[wangzhi_dict["backend"]][next_record] = {}
            backend_dict[wangzhi_dict["backend"]][next_record]["server"] = str(wangzhi_dict["record"]["server"])
            backend_dict[wangzhi_dict["backend"]][next_record]["weight"] = str(wangzhi_dict["record"]["weight"])
            backend_dict[wangzhi_dict["backend"]][next_record]["maxconn"] = str(wangzhi_dict["record"]["maxconn"])
    else:
        backend_dict[wangzhi_dict["backend"]] = {0:{"server":wangzhi_dict["record"]["server"],"weight":wangzhi_dict["record"]["weight"],"maxconn":wangzhi_dict["record"]["maxconn"]}}
        # 如果增加的网址不在back_dict中，就添加对应的网址信息和server信息

def del_html():
    "删除输入网址对应的信息"
    flag = 0
    wangzhi_dict = eval(input("请输入需要删除的网址信息:(例如:{'backend': 'www.oldboy.org','record':{'server': '100.1.7.9','weight': 20,'maxconn': 30}})"))
    if wangzhi_dict["backend"] in backend_dict:
        for i in backend_dict[wangzhi_dict["backend"]].keys():
            if backend_dict[wangzhi_dict["backend"]][i]["server"] == wangzhi_dict["record"]["server"]:    # 输入的网址中的server存在backend_dict中，做个标记，在下面删除
                del_flag = i
                flag += 1
        if flag != 0:
            del backend_dict[wangzhi_dict["backend"]][del_flag]
            print("已经成功删除！")
        if flag == 0:
            print("不存在输入的server！")
    else:
        print("不存在输入的网址！")

while True:
    reread()
    find_backend()
    choice = input("请输入你需要的操作:(显示:y 查询:s 增加:a 删除:d 退出:q)")
    if choice == "s":
        select_html()
    elif choice == "a":
        add_html()
        write_file()
    elif choice == "d":
        del_html()
        write_file()
    elif choice == "y":
        show_html()
    elif choice == "q":
        exit()
    file_list_new.clear()
    file_list.clear()