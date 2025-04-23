#install dropbox
#api key to dropbox


#install two library

import os
import dropbox
import dotenv

#dotenv.load_dotenv() loads the environment variables
#sensitive info such as API keys are stored in file .env , that is in the same directory level as working file.
#dotenv.load_dotenv() automatically looks for .env file in same directory.

dotenv.load_dotenv()

#use the variables that are loaded through os.getenv
ACCESS_TOKEN =os.getenv("ACCESS_TOKEN")

d = dropbox.Dropbox(ACCESS_TOKEN)

filepath = 'istockphoto-467367026-612x612.jpg'

#opening the file in rb mode, which mean read binary.
#'r':open file
#'b': binary mode.
#'rb' mode tells python to handle files as series of bytes instead of text.
#use this for handling images, documents (like PDFs), audio, video, or any non-text-based file types.


with open('files/istockphoto-467367026-612x612.jpg' , 'rb') as file:
    content = file.read()
    d.files_upload(content,f'/{filepath}' ,mode= dropbox.files.WriteMode('overwrite'))
    print(f"File {filepath} uploaded successfully!")
