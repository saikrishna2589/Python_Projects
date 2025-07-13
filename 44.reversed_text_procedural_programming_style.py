#below is procedural programming.
# we will convert the code below to object oriented code(class) in another python file.

with open('files/content_to_reverse_words','r') as file:
    content = file.read()

split_words = content.split()

reversed_word_list =[]

for word in split_words:
    word_reversed = word[::-1]
    reversed_word_list.append(word_reversed)

reversed_sentence = ' '.join(reversed_word_list)

print(reversed_sentence)

#create_new_file_with_reversed_words
with open('files/reversed_content_file_output','w') as file:
    file.write(reversed_sentence)


