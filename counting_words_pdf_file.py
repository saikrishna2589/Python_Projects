import pdfplumber
import json

file = 'pdf/Sharding.pdf'


content ={}

with pdfplumber.open(file) as pdf:
    pages = pdf.pages  #creates list of page(s) object

    for i, page in enumerate(pages):
        text = page.extract_text()
        content[i] = text


#saving as json
with open('sharding_slides.json', 'w', encoding ='utf-8') as file:
    json.dump(content,file,indent=4, ensure_ascii=False)
