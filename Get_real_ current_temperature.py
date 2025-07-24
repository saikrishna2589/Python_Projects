#endpoint
import requests
import os
from dotenv import load_dotenv


#load environmental variables from env file
load_dotenv() #load environmental variables

API_key = os.getenv('API_key')

def get_temperature(city):
    base_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric"
    response = requests.get(base_URL)
    data = response.json()
    weather_status = data['weather'][0]['main']
    temp_status = data['main']['temp']
    return f"weather is {weather_status} and temperature is {temp_status}"


city = input("enter the city name: ").title()
call_function = get_temperature(city)
print(call_function)

