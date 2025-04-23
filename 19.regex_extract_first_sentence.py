import re
import os

dir_name = 'regex_project_first_sentence'
file_list = os.listdir(dir_name)
first_sentences = []

for file in file_list:
    file_path = os.path.join(dir_name, file)

    with open(file_path, 'r') as file_object:
        file_content = file_object.read()
        pattern = r'[^.!?]*[.!?]'
        extract_content = re.search(pattern, file_content)
        if extract_content:
            first_sentences.append(extract_content.group())

for first_sentence in first_sentences:
    print(first_sentence + "\n")
