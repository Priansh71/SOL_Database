import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()

new_rows= [('100.01.01.09','abc.com',100),
           ('100.10.10.12','xyz.com',102)]

cur.executemany("insert into 'ips' values(?,?,?)",new_rows)
con.commit()

cur.execute("select * from 'ips'")
print(cur.fetchall())
