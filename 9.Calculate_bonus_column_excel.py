import pandas as pd

#read excel files

salary_info = pd.read_excel('files/employee_data.xlsx')

print(salary_info)

#see info on the dataset

salary_info.head()
salary_info.info()

print(salary_info.describe())

#process the data .Transformation phase

salary_info['Bonus']  = salary_info['Salary'] * 0.1

print(salary_info)


#export to excel

print(type(salary_info))

salary_info.to_excel('files/employee_data_moded.xlsx' , sheet_name = 'employee_bonus', index = False)