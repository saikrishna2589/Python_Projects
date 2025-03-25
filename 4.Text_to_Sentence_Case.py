
filepath = r"C:\Users\ssamudrala\Downloads\snowwhite.txt"

with open(filepath, "r") as file:
    snowwhite = file.read()

print(snowwhite)

#capitalise first word after each sentence.
#method- split at each sentence

#pass the text and output should be capitalised first word.

def capitalise_first_word(text_content):
    sentence_list = text_content.split('. ')
    make_first_word_cap = [sentence.capitalize() for sentence in sentence_list]
    make_sting_again = ".".join(make_first_word_cap)
    with  open('snowwhite_corrected_text_1.xlsx', 'w') as corrected:
        corrected.write(make_sting_again)



#test = capitalise_first_word(snowwhite)

capitalise_first_word(snowwhite)

