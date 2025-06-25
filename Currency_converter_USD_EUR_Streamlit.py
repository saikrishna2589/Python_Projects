

import streamlit as st
import requests

api_key ="600547bb486839e4b4a30ee4"
URL =  f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"




st.title("Currency converter : USD -- EUR")
user_selection = st.radio("Select the Currency conversion", ("USD to EUR" , "EUR to USD")) #USD to EUR
numerical_user_input = st.number_input("Enter the amount")  #10
button = st.button("Convert")

def conversion_function(currency, numerical_input):
    if currency == user_selection[:3]:
        response = requests.get(URL)
        data_json = response.json()
        output_data = data_json['conversion_rates']['EUR'] * numerical_user_input
        return f"{output_data :2f}"

    else:
        response = requests.get(URL)
        data_json = response.json()
        output_data = numerical_user_input / data_json['conversion_rates']['EUR']
        return f"{output_data :.2f}"



if user_selection =="USD to EUR":
    if button:
        convert_function_result = conversion_function(user_selection[:3], numerical_user_input)
        st.success(f"{numerical_user_input} {user_selection[:3]}"
                   f" is equal to {convert_function_result} {user_selection[-3:]}")
else:
    if button:
        convert_function_result =  conversion_function(user_selection[-3:] , numerical_user_input)
        st.success(f"{numerical_user_input} {user_selection[-3:]} is equal to"
                   f" {convert_function_result} {user_selection[:3]}")










