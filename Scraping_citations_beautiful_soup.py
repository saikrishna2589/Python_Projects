from Beautiful_Soup_Scraping_Text_from_Website import beautifulsoup_object

#class method finds only the first element that has the specific class
#here we want to find citations from a topic(mathematics) on wikipedia page.
# so we need multiple elements , not just one. we can use either 'find all' method
#or select method in beautiful soup


url = 'https://en.wikipedia.org/wiki/Mathematics'

#extract citations

import requests
from bs4 import BeautifulSoup

# step 1 -->Extract source code

response = requests.get(url).text
#convert the sourcecode to beautiful soup object
#step 2w

beautifulsoup_object_conversion = BeautifulSoup(response,'html.parser')

#now we can access the beautiful soup methods

select_citations = beautifulsoup_object_conversion.select("li[id^='cite_note']")

print(type(select_citations))


#saving in file
with open('citations.txt','w',encoding='utf-8') as file:
    for i in select_citations:
        file.write(i.get_text()+"\n")