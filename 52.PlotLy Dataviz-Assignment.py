import plotly.express as px # plot the data in the file
import pandas as pd  # read the data file

data_loc = 'files/employees (1).csv'

data = pd.read_csv(data_loc,index_col = 'EmployeeID')

salary_performance_viz = px.scatter(data,x='PerformanceScore', y='Salary',color='Department',
                                    title = 'Salary vs Performance',
                                    hover_data=
                                    {'Name':True,
                                     'Salary':True,
                                     'PerformanceScore':True,
                                     'Age':False})

salary_performance_viz.show()