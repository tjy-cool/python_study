#!/usr/bin/env python
# Funtion:      
# Filename:

import configparser

config = configparser.ConfigParser()

config['DEFAULT'] = {}
config['DEFAULT']['install'] = 'yes'
config['DEFAULT']['PATH'] = 'C:/user/python'
config['DEFAULT']['forwardx11'] = 'yes'

config['www.baidu.com'] = {
    'Host port':'502',
    'forwardx11':'NO',
}

config['topsecrt.server.com'] = {}
topsecrt = config['topsecrt.server.com']
topsecrt['Host Port'] = '8080'
topsecrt['user'] = 'tjy'

with open('new_config.ini','w',encoding='utf-8') as f:
    config.write(f)