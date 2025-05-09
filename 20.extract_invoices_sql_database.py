import sqlite3
data_loc = 'data_invoice.db'

#create connection
conn = sqlite3.connect(data_loc)

#create cursor
cursor = conn.cursor()

#query
query ="""
SELECT * FROM invoices
WHERE BillingCountry = "Germany" AND Total > 2
"""
#execute query
query_execute = cursor.execute(query)

#data fetch
data_extract = query_execute.fetchall()

for data in data_extract:
    print(f"{data[0]}")

#close the connection
conn.close()