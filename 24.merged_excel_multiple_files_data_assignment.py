# create a dataframe for the data within each excel.
import os
import pandas as pd

#input?
directory_files = 'project_excel_files_data_merge'

#create a list of filenames
file_names = os.listdir(directory_files)

file_path = [os.path.join(directory_files, file) for file in file_names]

#create an empty list
file_2024_content = []
file_2025_content=[]

for each_file_path in file_path:
    if each_file_path.endswith('2024.xlsx'):
        #read excel
        file_content = pd.read_excel(each_file_path, engine='openpyxl')
        file_2024_content.append(file_content)

#merging the 2024 files data into one dataframe

df_2024 = pd.concat(file_2024_content , ignore_index=True)


#exporting 2024 data to excel
df_2024.to_excel('project_excel_files_data_merge/2024_merged_data.xlsx', index=False)


#repeat the same for 2025 file

for each_file_path in file_path:
    if each_file_path.endswith('2025.xlsx'):
        #read excel
        file_content = pd.read_excel(each_file_path, engine='openpyxl')
        file_2025_content.append(file_content)

#merging the 2025 files data into one dataframe

df_2025 = pd.concat(file_2025_content , ignore_index=True)


#exporting 2024 data to excel
df_2024.to_excel('project_excel_files_data_merge/2024_merged_data.xlsx', index=False)
df_2025.to_excel('project_excel_files_data_merge/2025_merged_data.xlsx', index=False)


