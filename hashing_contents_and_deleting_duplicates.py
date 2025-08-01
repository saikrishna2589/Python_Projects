import os
import hashlib

directory ='files/detect_duplicate_files'

#walk through the directory, get the root, sub-dir and files
#get the files
#create filepath
#read the contents
#pass contents to dict
#if key already in dict, flag duplicate and then delete the duplicate file
#print message of deletion
#then print the files now finally in the folder after de-duplication

#function to read file contents in binary format
def hashed(file_path):
    with open(file_path, 'rb') as filecontent:
        file_content = filecontent.read()
        hashed_content = hashlib.sha256(file_content).hexdigest()
        return hashed_content


hashedcontent_store = {}
deleted_files =0
files_remaining=0
file_folder = os.walk(directory)

for root, dir, files in file_folder:
    for file in files:
        # filepath build
        filepath = os.path.join(root,file)
        #read files in binary mode to get underlying contents access
        hashed_data = hashed(filepath) #finished reading content.

        if hashed_data in hashedcontent_store:
            #delete file
            os.remove(filepath)
            deleted_files +=1
            print(f"Duplicate file : {filepath} has been deleted")

        else:
            hashedcontent_store[hashed_data] = filepath


print(f"The remaining deduplicated files:\n ")

for root,dir, files in os.walk(directory):
    for file in files:
        files_remaining += 1
        print(os.path.join(root,file))

print(f"files remaining in the folder:{files_remaining}")
print(f"deleted files: {deleted_files}")






