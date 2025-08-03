from bs4 import BeautifulSoup
import requests
url ="https://forecast.weather.gov/MapClick.php?lat=40.7130466&lon=-74.0072301"

#you want to save the content of the webpage into python.
#1t step get source code of webpage--> use requests library for that.


#once you have source code, you can extract the tempearture value using BeautifulSoup

#step1
content = requests.get(url)
response = content.text   #.content is for pdf webpages or images.

response1= content.headers['Content-Type']
print(response1)
#.text is for html text

#now that you have source code, use beautiful soup to extract temperature of NY city from the source code

#step2
#convert the html text into beautiful soup object and extract the temp value

beautifulsoup_object = BeautifulSoup(response,'html.parser')
print(beautifulsoup_object) # beautiful soup object is created on the html text.

# we can now use methods of beautfiul soup like find method

temperature_value = beautifulsoup_object.find(class_ = 'myforecast-current-lrg').get_text()

print(temperature_value)