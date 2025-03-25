#read data

import pandas as pd

order_details = pd.read_excel('files/Input.xlsx')

print(order_details.head())

#transform the data(process the data)

order_details['Total_Revenue'] =  order_details['Price'] * order_details['Quantity']


#export the data out
order_details.to_excel('files/Input.xlsx', sheet_name = 'order_details')#,index = False )
