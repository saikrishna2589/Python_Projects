
#2 STEPS
#Step 1 : import the source code
#Step 2 : convert to beautiful soup object and use find or select methods to extract the paragraphs

from bs4 import BeautifulSoup
import requests

url ='https://en.wikipedia.org/wiki/Mathematics'

#step 1:source code retreival

response = requests.get(url).text

#convert response to bs object

beautiful_soup_object = BeautifulSoup(response,'html.parser')

para_finder = beautiful_soup_object.select('p')

with open('para.txt', 'w',encoding='utf-8') as file:
    for para in para_finder:
        file.write(para.get_text() +'\n')

