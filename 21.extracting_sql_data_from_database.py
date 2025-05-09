#library to read sql data
import sqlite3

#input data
dbfile = 'data.db'


# 4 steps to connect and query  sql data
    #1) create connection to db ;
    #2) create a cursor (Middleman that communicates query to db)
    #3) create a query
    #4) extract the data by passing the query to the cursor


conn = sqlite3.connect(dbfile)
cursor = conn.cursor()

query ="""
SELECT * FROM albums
WHERE Title LIKE "%Live%" AND LENGTH(Title)>10
"""

#execute the query
data_output = cursor.execute(query)

#fetch the data
data_fetch =  data_output.fetchall()

for row in data_fetch:
    print(f"{row[0]} : {row[1]}")


