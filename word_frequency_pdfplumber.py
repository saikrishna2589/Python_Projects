import pdfplumber

file_loc ='pdf/pdf1 (1).pdf'

#frequnecy word -->word count
list_of_each_word = []
word_count= {}

#opened the pdf file ,save contents in a list
with pdfplumber.open(file_loc) as file:
    list_pages = file.pages
    for page in list_pages:
        content = page.extract_text().lower().strip()
        word_list = content.split()
        list_of_each_word.extend(word_list)


#cleanse the words

#loop through list of words and add key and frequency into dictionary

for word in list_of_each_word:
    word = word.strip(".,?/")
    word_count[word] = word_count.get(word,0)+1

    #alteratively below
    #if word in word_count:
        #word_count[word] +=1
    #else:
        #word_count[word] = 1


#so now each word frequency is stored.

for key in word_count:
    print(f"{key} : {word_count.get(key,0)}")

user_input = input('Enter the word you want to search for: ').lower()

def word_count_output(word):
    return word_count.get(word,0)

print(f"'{user_input}' word is repeated {word_count_output(user_input)} times")







