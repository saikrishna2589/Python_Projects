import streamlit as st
from faker import Faker

fakename_class =Faker()

random_name_list = []

def generate_names(number_of_names):  #function need to do just 1 thing well so this function is generating nae .
    for i in range(number_of_names):
        name = fakename_class.name()
        random_name_list.append(name)


user_input_number = st.number_input("Enter the number of names you want to generate",
                                    min_value=1,
                                    max_value=100,
                                    step=1)


button = st.button("Generate names")

if button:
    generate_series = generate_names(user_input_number)
    st.subheader("Generated names")
    for each_name in random_name_list:
        st.write(each_name)






