#!/usr/bin/env python
# Funtion:      
# Filename:

import configparser
config = configparser.ConfigParser()

config.read('config.ini')
# print(config.sections())
# print(config.defaults())
# print(config.default_section)

section_name = config.sections()[1]
print(section_name)     # topsecret.server.com
print(config[section_name]['host port'])    # 打印host port对应的值

print(config.options(section_name)) # 打印default和本section里面的key

# config.remove_option(section_name, '')

config.write(open('config2.ini', 'w'))
# for i,v in config[section_name].items():
#     print(i,v)