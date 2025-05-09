import os

import pandas as pd

directory_path =  'excel_files'

#this gives a list of file names
file_name = os.listdir(directory_path)
file_contents = []

for file in file_name:
    #file_path = [os.path.join(directory_path,file) for  file in file_name]
    file_path = os.path.join(directory_path, file)

    #Open the excel files as data frames
    read_file_content = pd.read_excel(file_path , engine= 'openpyxl')
    file_contents.append(read_file_content)


if file_contents:
    combined_df = pd.concat(file_contents, ignore_index=True)


combined_df.to_excel('excel_files/merged_files.xlsx',index=False)