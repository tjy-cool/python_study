#!/usr/bin/env python
# Funtion:      
# Filename:

import urllib.parse
import urllib.request
import json
import csv

# url = 'http://IP:PORT/xxx'
url = 'http://IP:PORT/xxx'

with open("全2014.csv", 'r', encoding='utf-8') as f:
    reade1 = csv.reader(f)
    print(type(reade1))

    # for row in reader:
    #     print(row)

#
# # 接收的数据
# recv_data = urllib.request.urlopen(url).read()
#
# #############
# # 在此处对接受的数据recv_data进行解码
# ##############
# # 在此处对结果进行计算
# #############
# # 在此处将计算结果组合成JSON格式
# # 现假设已经弄好了，数据格式为 send_data
#
# send_data = {
#     {
#         'time': "2017-09-06 02",
#         'PM10': 20,
#         'PM25': 23,
#         'so2':10,
#
#         '预报风速': 0.7
#     },
#     {
#         'time': "2017-09-06 03",
#         'PM10': 10,
#         'PM25': 22,
#         'so2': 13,
#
#         '预报风速': 0.2
#     }
# }
#
# #将POST值URL编码, 并编码为 utf-8格式
# send_format_data = urllib.parse.urlencode(send_data).encode('utf-8')
#
# #发送POST请求
# req = urllib.request.Request(url, send_format_data)
#
#
#

