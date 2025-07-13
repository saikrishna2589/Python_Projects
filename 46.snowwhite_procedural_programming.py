# Read the text from the file
with open("snowwhite.txt", "r") as f:
    text = f.read()

# Split the text into sentences and capitalize the first letter of each sentence
sentences = text.split(". ")
corrected_sentences = []
for sentence in sentences:
    corrected_sentences.append(sentence.capitalize())
corrected_text = ". ".join(corrected_sentences)

# Write the corrected text to a file
with open("snowwhite_corrected.txt", "w") as f:
   f.write(corrected_text)
