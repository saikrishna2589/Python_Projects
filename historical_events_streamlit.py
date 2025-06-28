import streamlit as st
import requests

import requests


st.title ("Check historical events for the month and date of interest")


month_input_entry = st.number_input("Enter the month number")
date_input_entry = st.number_input("Enter the date")

button = st.button("Show Events")

extract =[]

def historical_events(month_input, date_input):
    url_historical_events = f"http://history.muffinlabs.com/date/{month_input}/{date_input}"

    response = requests.get(url_historical_events)
    data_response = response.json()
    data_output = data_response["data"]["Events"]

    for event in data_output:
        extract.append(f"year: {event["year"]} \n"
                       f"Description: {event["text"]}\n")

    return extract

if button:
    historical_events_function = historical_events(month_input_entry,date_input_entry)
    for each in extract:

        st.write(each)










