import streamlit as st

directory_path ='plot_files'
import glob

file_path = glob.glob(f'{directory_path}/*.txt')

content_dict ={}

for each_file_path in file_path:
    with open(each_file_path, 'r') as file:
        content = file.read()
        key,value = content.split(':')
        content_dict[key] =float(value)

#I so far create list of file paths, read the data,
# split the content, assigned to dic key,value pairs
print(content_dict)

dict_convert_format ={
    "x-axis" :list(content_dict.keys()),
    "y-axis" : list(content_dict.values())
}



st.title("Plot Line chart using Streamlit")

st.line_chart(dict_convert_format,x = "x-axis")


