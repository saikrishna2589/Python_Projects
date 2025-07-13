import streamlit as st
import pandas as pd

file ='files/martian_data.csv'


load_csv = st.file_uploader('Please upload your csv file',
                            type='csv')

if load_csv is not None:
    data = pd.read_csv(load_csv)

    preview_data = data.head()
    st.success("file uploaded successfully!")
    preview = st.dataframe(preview_data)

    print(data.columns)

    selected_column = st.selectbox("Select a column", list(data.columns[1:]))

    st.write(f"selected column: {selected_column}")
    min_value = data[selected_column].min()
    max_value = data[selected_column].max()

    store= (min_value, max_value)
    slider_values = st.slider("select the range",min_value, max_value,store)

    st.write(f"slider_values:{slider_values}")


    #filter the df now based on slider values

    df_filtered = data[data[selected_column].between(slider_values[0]
                                                     , slider_values[1])]

    st.write(df_filtered.head())

    x_axis = (list(df_filtered.columns)[0])

    # now the line graph
    st.line_chart(df_filtered.set_index(x_axis)[selected_column],
                  x_label='Date',y_label=f"{selected_column}")








