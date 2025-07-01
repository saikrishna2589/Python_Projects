import streamlit as st

import glob
import os

from isort.parse import file_contents

dir_location = 'plot_streamlit_assignment'
#list of filenames

filename_list = glob.glob(f"{dir_location}/*.txt")
print(filename_list)

#loop through the list of filenames
#and extract filename

filenames =[]

for filename in filename_list:
    file_name = os.path.basename(filename)
    filenames.append(file_name.replace(".txt",''))

#read content in the files
file_contents =[]

for file_path in filename_list:
    with open(file_path,'r' ) as file:
        file_content = file.read()
        file_content = float(file_content)
        file_contents.append(file_content)


dict_output = dict(zip(filenames,file_contents))


dict_plot = {
    "x-axis": list(dict_output.keys()),
    "y-axis":list(dict_output.values())
}
st.title("plot line chart on streamlit")

st.line_chart(dict_plot, x="x-axis")

st.write('key:value pairs of line plot are below:\n')

for key,value in dict_output.items():
    st.write(f"{key}:{value}")










