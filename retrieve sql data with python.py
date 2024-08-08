import sqlite3
#Establist a conection and create a cursor 
con = sqlite3.connect('database.db')
# cur is cursor object
cur = con.cursor()

#Execute sql - get all rown and colum in order
cur.execute("SELECT * FROM 'ips' ORDER BY asn")
print(cur.fetchall()) # fetchall() is a method
#the output is a list of tuple, each tuple is a row 

# get all rows and certain columns
cur.execute("SELECT address, asn FROM 'ips' ORDER BY asn")
print(cur.fetchall()) 

# get all rows and certain columns where asn <300
cur.execute("SELECT * FROM 'ips' where asn<300 ")
print(cur.fetchall()) 

# get all rows and certain columns where asn <300 and domain with a certain words
cur.execute("SELECT * FROM 'ips' where asn<300 AND DOMAIN LIKE '%sa' ")
# print(cur.fetchall()) 
result1 = print(cur.fetchall()) 
print(result1)
# Gives list as output
result2 = print(cur.fetchall())
print(result2)
# Returns empty list as for a single query it can only be executed once

for row in result1:
  print(row)
# We will get tuples in different row


