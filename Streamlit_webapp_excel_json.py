from distributed.dashboard.scheduler import applications
from streamlit import download_button

from Excel_to_JSON_WEB_APP import excel_to_json

import streamlit as st


st.header('Excel to JSON file converter')
st.write('Upload excel file to convert to JSON')

file_upload = st.file_uploader(
    "Choose an excel file to upload." ,
                               type=['xlsx','xlx'])

if file_upload is not None:
    json_format = excel_to_json(file_upload)
    st.json(json_format)
    st.download_button(download_button='Download',
                       data = json_format,
                       file_name = 'json_format_countries',
                       mime =  'application/json')







