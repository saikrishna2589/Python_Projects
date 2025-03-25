import os
from datetime import datetime

#aim is to build file path for current files
#for loop
#new file name would be constructed using f string .
#then construct new file path using os.path.join

current_directory = 'files_date_project'

#create a list of files in the directory so as to loop ove rename each one
files_list_convert = os.listdir(current_directory)

#loop through each file in the list now

for file in files_list_convert:
    new_file_part = file[:-4]
    current_date = datetime.now().strftime("%Y-%m-%d")

    #constructing the new file name
    new_file_name = f"{new_file_part}-{current_date}.txt"



    current_file_path = os.path.join(current_directory, file)
    #specify the new path that includes new file name
    new_file_path = os.path.join(current_directory, new_file_name)

    print(current_file_path)
    print(new_file_path)

    #renaming the current path to new path for each file
    #so we do all this steps within for loop on each file
    os.rename(current_file_path, new_file_path)

    print(f"filename changed from {file} to {new_file_name}")
