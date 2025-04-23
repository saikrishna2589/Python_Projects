import requests

country = (input('Enter your country: ').strip())
url = f'https://restcountries.com/v3.1/name/{country}'

response = requests.get(url)

data = response.json()


for item in data:

    #'captial' is a list, so converting to a string using join method
    Capital= ", ".join(item.get('capital',['No capital found']))
    print(f"Capital: {Capital}")
    Region = item.get('region', 'No region found')
    Population = item.get('population' , 'No population found')
    Languages_list = list(item['languages'].values())
    Languages_string = ", ".join(Languages_list)

    print(f"Region: {Region}")
    print(f"Population: {Population}")
    print(f"Languages: {Languages_string}")


