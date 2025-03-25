
filepath = r"C:\Users\ssamudrala\Downloads\example.txt"

with open(filepath, "r") as file:
    file_content = file.read()

list_of_words = file_content.split()

#looping through each word in the list to reverse the word
##Using word slicing and step -1
reverse_word_list =[]
for word in list_of_words:
    reverse_word = word[::-1]
    reverse_word_list.append(reverse_word)

#convert from list to string so as to write contents to new file.
# we use string method " ".join(reverse_word_list)


reversed_content =  " ".join(reverse_word_list)

print(reversed_content)
#writing to new file
with open("reversed_content_file" , "w") as reversed:
    reversed.write(reversed_content)