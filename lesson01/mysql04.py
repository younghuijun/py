# encoding: utf-8
#!/usr/bin/python

import MySQLdb

db = MySQLdb.connect('localhost','root','root','test')

cursor = db.cursor()

sql = 'select * from t_test'


#print('total row count:' + result.rowcount)

cursor.execute(sql)

result = cursor.fetchall()

for row in result:
    print row[1]
        
db.close()
    