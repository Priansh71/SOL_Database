import sqlite3 
import pandas as pd 


con = sqlite3.connect('database.db')
cur = con.cursor()

pandas.read_sql_query("SELECT * FROM 'IPS' ORDER BY asn" , con) # con is the object to specify which connection is specified
print(df)

df.to_csv('database.csv',index=NONE)
# Before this install 
# pip install openpyxl
df.to_excel('database.xlsx',index=NONE)
