import os
import requests
from dotenv import  load_dotenv

load_dotenv()    #this just loads the environment variables
api_key = os.getenv('API_KEY')


def get_celsius_fahrenheit(place):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    celsius =  data['main']['temp']
    ask_user = input('Choose temperature Unit (C for Celsius , F for Fahrenheit): '  ).strip().upper()

    if ask_user =="C":
        return round(celsius,2)

    elif ask_user =="F":
        fahreinheitconversion = (float(celsius) *9/5) +32
        return round(fahreinheitconversion,2)
    else:
        return "Invalid Selection . Choose 'C' or 'F'."


user_input_city = input("Enter the city: ").strip().title()
output = get_celsius_fahrenheit(user_input_city)


print(f"Current temperature in {user_input_city} is {output} ")





