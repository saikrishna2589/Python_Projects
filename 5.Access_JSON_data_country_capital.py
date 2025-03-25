country='India'

import requests
url= "https://restcountries.com/v3.1/all"
response = requests.get(url)

json_content = response.json()

print(json_content)

while True:
    user_country = input("Enter the name of your country: ")

    country_found = False

    for country in json_content:
        name_country= country['name']['common']
        if name_country.lower() == user_country.lower():
           # .get method below is dictionary method
           #if capital key doesn't exist for any country while looping,
           #it doesn't produce an error.Instead it take the default value
           #"Unknown"
            capital =  country.get('capital',"Unknown")[0]
            print(f"The capital of {name_country} is {capital}")
            country_found = True

    if not country_found :  #equivalent to if not True then print
        print(f"country {user_country} doesn't exist")
