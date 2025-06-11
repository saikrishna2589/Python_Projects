import re  # for regex-based sentence splitting

# Prompting the user to enter multiple lines of text
print("Enter your text. Type/Paste each sentence separately (press 'Enter' twice to exit): ")

# Step 1: Capture all user input lines
sentences = []
while True:
    user_input = input()
    if user_input:
        sentences.append(user_input)
    else:
        break  # break when Enter is pressed twice (blank input)

# Step 2: Join all the lines into a single paragraph
final_sentence = " ".join(sentences)

# Step 3: Function to remove basic punctuation from the text
def remove_punctuation(text):
    punctuations = "./?,"
    for char in punctuations:
        text = text.replace(char, "")
    return text  # Note: This should be outside the loop to apply all punctuation replacements

# Clean the final text
final_sentence = remove_punctuation(final_sentence)

# Step 4: Calculate total number of characters in the cleaned sentence
number_of_char = len(final_sentence)

# Step 5: Split the sentence into words to count total words
word_list = final_sentence.split()
word_count = len(word_list)

# Step 6: Split original sentence into sentence fragments using punctuation
# We use regex to split by `.`, `!`, or `?`
sentence_split = re.split(r"[.!?]", final_sentence)

# Step 7: Clean empty strings from sentence list
cleaned_sentence_list = []
for each_sentence in sentence_split:
    if each_sentence.strip():  # remove empty or whitespace-only strings
        cleaned_sentence_list.append(each_sentence.strip())

# Step 8: Count the number of sentences
total_sentences = len(cleaned_sentence_list)

# Step 9: Count the frequency of each word
dict_of_words = {}
for word in word_list:
    if word not in dict_of_words:
        dict_of_words[word] = 1
    else:
        dict_of_words[word] += 1

# Step 10: Find the most frequent word
most_frequent_word = max(dict_of_words, key=dict_of_words.get)

# Step 11: Average word length (Method 1): using total characters and word count
Avg_word_length = number_of_char / word_count

# Step 12: Average word length (Method 2): using sum of lengths of each word
length_of_each_word = [len(word) for word in word_list]
avg_word_length_2 = sum(length_of_each_word) / len(word_list)

#Step 13: Average sentence length

Avg_sentence_length = word_count / len(sentences)
# Final Output
print("\nText Analysis Results:")
print("-" * 30)
print(f"Total Characters (no punctuation): {number_of_char}")
print(f"Total Words: {word_count}")
print(f"Total Sentences: {total_sentences}")
print(f"Cleaned Sentence List: {cleaned_sentence_list}")
print(f"Most Frequent Word: '{most_frequent_word}' occurred {dict_of_words[most_frequent_word]} times")
print(f"Average Word Length (Method 1): {Avg_word_length:.2f}")
print(f"Average Word Length (Method 2): {avg_word_length_2:.2f}")
print(f" Average_words_per_sentence: {Avg_sentence_length}")

