#!/usr/bin/env python
# Funtion:      
# Filename:

import configparser
config = configparser.ConfigParser()

config.read('new_config.ini')
#
# # 查询方法
# print(config.sections())    # 打印所有的section，为列表
# conf_section = config.sections()[0] # 取出section里的第一个元素
# print(config.options(conf_section))     # 打印该section下面所有的option
# # 遍历查询options
# for i,v in config[conf_section].items():
#     print("%s:%s" % (i,v))

# 单个查询options的值
# baidu = config['www.baidu.com']
# print(baidu['host port']) # 打印section下的option为host port 的值
# print(baidu['path'])
# print(config['www.baidu.com']['install'])

# 删除section
sec = config.remove_section('www.baidu.com')    # 存在返回True并删除，否则返回False无任何操作
print(sec, config.sections())

# 删除options
section = config['topsecrt.server.com']
print(section.name)
options = config.remove_option('topsecrt.server.com', 'haha')   # 存在返回True并删除，否则返回False无任何操作
for i,v in section.items():
    print("%s:%s" % (i,v))

# 设置options的值
# config.set(section.name,'install', "no")
# for i,v in section.items():
#     print("%s:%s" % (i,v))


# # 增加section
# config.add_section('www.google.com')
# print(config.sections())


