import streamlit as st
import pandas as pd

file_upload = st.file_uploader('Upload the csv file', type='csv')

if file_upload is not None:
    st.title("Employee Metrics Internal Dashboard")
    data = pd.read_csv(file_upload)
    st.write("Data:\n")
    st.write(data.head())

    numeric_columns = list(data.select_dtypes(include=["number"]).columns)[1:]
    st.write(numeric_columns)
    selected_column= st.selectbox("Select the column of interest",numeric_columns)

    st.line_chart(data.set_index(list(data.columns)[0])[selected_column])

    st.write('choose x and y axis for scatter plot\n')
    st.write('x-:axis:\n')
    selected_x_axis = st.selectbox("choose x-axis",numeric_columns)
    st.write('y-axis:\n')
    selected_y_axis =  st.selectbox("choose y-axis",numeric_columns )

    st.scatter_chart(data, x= selected_x_axis ,
                     y=selected_y_axis,
                     x_label=f"{selected_x_axis}",
                     y_label =f"{selected_y_axis}")

