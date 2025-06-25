
from excel_to_csv_backend_code import excel_to_csv
import streamlit as st

heading = st.title (" Excel to CSV Converter")
description = st.header ("Upload an Excel file to convert to CSV")

file_uploader = st.file_uploader("Select an excel file to be uploaded" ,
                                 type=['xlsx','xlx'])

if file_uploader is not None:
    uploaded_file = excel_to_csv(file_uploader)
    download_data = st.download_button('Download',
                                       uploaded_file ,
                                       file_name='file_csv',
                                       mime = 'text/csv')

