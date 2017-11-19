import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='lemaker')
cursor = conn.cursor()

data = [
    ("N1", "2017-1-23", "M"),
    ("N2", "2017-1-23", "M"),
    ("N3", "2017-1-23", "M"),
]

cursor.executemany('insert into student (name, register_date, gender) values (%s, %s, %s), data')

conn.commit()
