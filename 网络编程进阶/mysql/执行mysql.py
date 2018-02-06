#!/usr/bin/env python
# Funtion:      
# Filename:

import pymysql
conn = pymysql.connect(host = 'localhost', port = 3306,
                       user = 'root', passwd = 'lemaker',
                       db = 'test_20180122', charset = 'utf8')

cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)

# 执行SQL，并返回收影响行数
effect_row = cursor.execute('show databases;')
print('effect_row: ', effect_row)

all_row = cursor.fetchall()
print(all_row)

# 执行SQL，并返回受影响行数,执行多次
# effect_row = cursor.executemany()

cursor.close()
conn.close()
