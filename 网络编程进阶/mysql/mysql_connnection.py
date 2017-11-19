import pymysql
# 创建连接
conn = pymysql.connect(host='localhost', port=3306,
                       user='root', passwd='lemaker')
# 创建游标
cursor = conn.cursor()
# 执行SQL，并返回受影响行数
effect_row = cursor.execute("show databases;")
print(cursor.fetchone())

print(cursor.fetchall())

cursor.close()
conn.close()
