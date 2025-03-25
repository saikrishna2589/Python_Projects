
#rename the files in the directory to filename-wordcount-weekdayname

#for stringing the filepath to the filenames

import os
from datetime import datetime
import time

current_file_directory = 'files'


#create a list of filenames in the directory
current_file_name =  os.listdir(current_file_directory)


# constructing the file path now to loop through each path

for filename in current_file_name:
    current_file_path = os.path.join(current_file_directory,filename)

    #open each file to get the word count.pass this filepath to with context manager
    with open(current_file_path , 'r') as file_path:
        content = file_path.read()

        #Ensure file is closed before renaming
        time.sleep(0.5)  #msall delay to allow OS to release file lock

        strip_content = content.split()  #splitting each word and making a list
        word_count = len(strip_content)  #counting the length of the split words

        current_day = datetime.now().strftime("%A")

    #construct new filename

        new_file_name_part = filename[:-4]
        new_file_name = f"{new_file_name_part}-{word_count}-{current_day}.txt"


#close the file and then build new file path and rename the file
    new_file_path = os.path.join(current_file_directory ,new_file_name)

    os.rename(current_file_path , new_file_path)
    print(f"renamed {filename} to {new_file_name}")



