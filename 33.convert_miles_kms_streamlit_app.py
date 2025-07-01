import streamlit as st
from kms_to_miles_viceversa_conversion_backend_function import kilometers_miles_converter


st.title("Kilometers ⇄ Miles Converter")

user_selection = st.radio("Conversion units" , ("kms to miles", "miles to kms"))


if user_selection=="kms to miles":
    user_numerical_input = st.number_input("Enter the distance in kms")
    button = st.button("convert")

    if button:
       conversion_function_kms_miles = kilometers_miles_converter(user_selection ,user_numerical_input)
       st.success(conversion_function_kms_miles)

else:
    user_numerical_input = st.number_input("Enter the distance in miles")
    button = st.button("convert")

    if button:
        conversion_function_kms_miles = kilometers_miles_converter(user_selection, user_numerical_input)
        st.success(conversion_function_kms_miles)









