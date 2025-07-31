# we need the content of each file

#1st step is getting the input --> i.e list of files

#so lets create file path
import os
directory ='files/detect_duplicate_files'



file_path= os.walk(directory) #generator object -->this is iteratable object#

def file_read(each_file_path):
  with open(each_file_path,'rb') as fileread:
        content = fileread.read()
        return content

#store content in dictionary
file_content ={}
for root, dir, files in file_path:
    for file in files:
        filepath = os.path.join(root, file) #got the file path., now read.
        read_file = file_read(filepath) #returns binary content . #readfile has the content# .

        if read_file in file_content:
            print(f"Duplicate file found - {filepath}")
            print(f"Original file - {file_content[read_file]}")
        else:
            file_content[read_file] = filepath




