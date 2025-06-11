import os

file_dir = 'text_frequency'

#create list of files

file_list = os.listdir(file_dir)

print(file_list)

dictionary_of_words = {}

#create file path
for file in file_list:
    file_path = os.path.join(file_dir, file)
    #read data
    with open(file_path ,'r') as file_data:
        file_content = file_data.read()
        list_of_words = file_content.split()

        # loop through the list of words
        for word in list_of_words:
            word = word.lower().strip()
            if word in dictionary_of_words:
                dictionary_of_words[word] +=1
            else:
                dictionary_of_words[word] =1




print(dictionary_of_words)

#storing dictionary into a new file

with open('text_frequency/word_frequency.txt', 'w') as file_output:
    for word, freq in dictionary_of_words.items():
        file_output.write(f'{word} : {freq}\n')

