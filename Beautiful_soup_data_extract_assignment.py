from bs4 import BeautifulSoup
import requests

lat =float(input('Enter latitude: '))
lon =float(input('Enter longitude: '))

url = f"https://weather.com/weather/today/l/{lat},{lon}"



#step1--:extracting the sourcecode html
response = requests.get(url)

type_content = response.headers["Content-Type"] #confirming html type text content

text_extract = response.text

#step2-->using beautifulsoup class to extract temperature value from the sourcecode

#convert to beatifulsoup object

bs_object_html = BeautifulSoup(text_extract , 'html.parser')
temp =bs_object_html.find(class_='TodayDetailsCard--feelsLikeTempValue--8WgHV')

if temp:
    temp_extract = temp.get_text()
    print(f"The temperature is {temp_extract}")

else:
    "Temperature not found!"