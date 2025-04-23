import requests

# Prompt the user to enter a country
country = input("Enter country: ")

# Get the data as JSON from the URL endpoint for the given country
url = f'https://restcountries.com/v3.1/name/{country}'
response = requests.get(url)
data = response.json()

# Extracting various country info such as name, capital, etc.
country_data = data[0]
name = country_data['name']['common']
capital = country_data['capital'][0]
region = country_data['region']
population = country_data['population']
languages = ', '.join(country_data['languages'].values())

# Printing the extracted info
print(f"Capital: {capital}")
print(f"Region: {region}")
print(f"Population: {population}")
print(f"Languages: {languages}")