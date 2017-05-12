#!/usr/bin/env python
# Funtion:      
# Filename:


import configparser
config = configparser.ConfigParser()

config['DEFAULT'] =  {'ServerAliveInterval': '45',
                      'Compression': 'yes',
                     'CompressionLevel': '9'}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'tjy'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'
topsecret['Forwardx11'] = 'no'

config['DEFAULT']['Forwardx11'] = 'YES'

with open('config.ini','w', encoding='utf-8') as configfile:
    config.write(configfile)
