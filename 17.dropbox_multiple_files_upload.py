
#libraries
import os
import dropbox
import dotenv

#load env variables from env file
dotenv.load_dotenv()

#access the env variables
access_key = os.getenv("ACCESS_TOKEN")


 # Initialize Dropbox client
d= dropbox.Dropbox(access_key)


# Directory containing files to upload
current_file_dir = 'files'

#create list of filenames
file_name_list = os.listdir(current_file_dir)


#construct file path
for file in file_name_list:
    file_dir = os.path.join(current_file_dir,file)
    with open(file_dir,'rb') as file_path:
        data = file_path.read()
        d.files_upload(data,f'/{file}' ,mode= dropbox.files.WriteMode('overwrite'))
        print(f"✅  File {file_dir} uploaded successfully!")




