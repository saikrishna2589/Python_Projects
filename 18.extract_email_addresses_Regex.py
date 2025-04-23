
import re
import os

# directory
file_dir = 'regex_email_exercise'

#input the files
#create a list of file name
list_files = os.listdir(file_dir)

all_emails =[]
# loop through the list , create file path, read content, extract email

for file in list_files:
    file_path = os.path.join(file_dir, file)
    #open file and read content
    with open(file_path, 'r') as file_object:
        file_content = file_object.read()

        #dig into the content to extract email
        pattern = r'[a-zA-Z0-9+-_.]+@[a-zA-Z0-9+-_.]+\.[a-zA-Z]{2,}'
        email_info = re.findall(pattern, file_content)

        # extend method appends the items of the list into another list
        #so it would be list of strings
        all_emails.extend(email_info)


print(all_emails)
