#!/usr/bin/env python
# Funtion:      
# Filename:

import pymysql

conn = pymysql.connect(host = '127.0.0.1', port = 3306,
                       user = 'root', passwd = 'lemaker',
                       db = 'test_20180122', charset = 'utf8')

# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)       # 以字典形式显示
cursor = conn.cursor()                                          # 以元组形式显示
# effect_row = cursor.execute("select * from school")
efect_row = cursor.execute('desc school;')
# print('----', effect_row)
# row_2 = cursor.fetchone()
# cursor.execute("insert into school (name, age, gender, register_date, phone, city) "
               # "values ('ty', 26, 'M', '2006-2-3', 1342134130, 'SH');")

# print('---', dir(cursor))

cursor.execute('select * from school;')
row_1 = cursor.fetchone()
print(row_1)
row_2 = cursor.fetchone()
print(row_2)

cursor.scroll(-2, mode='relative')
# cursor.scroll(0, mode='absolute')
row = cursor.fetchone()
print(row)
# all_row = cursor.fetchall()
# for table in all_row:
#     print(table)

# print(all_row)
# print(all_row[0])

# conn.commit()

cursor.close()
conn.close()

# 获取自增ID
new_id = cursor.lastrowid
print(new_id)