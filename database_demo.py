# Author: Allen Anker
# Created by Allen Anker on 14/08/2018
import pymysql

'''
db = pymysql.connect(host='localhost', user='root', password='ASDFJKLP@189cf', port=3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:', data)
cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')
db.close()
'''

db = pymysql.connect(host='localhost', user='root', password='ASDFJKLP@189cf', port=3306, db='spiders')
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL,' \
      ' age INT NOT NULL, PRIMARY KEY (id))'
cursor.execute(sql)
sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
id, user, age = '20120001', 'Allen', 19
try:
    cursor.execute(sql, (id, user, age))
    db.commit()
except:
    db.rollback()
db.close()
