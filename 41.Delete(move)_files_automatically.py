import os
import shutil

directory_main = 'Downloads_test'

for root,directory,files in os.walk(directory_main):
    #print(f"root: {root}")
    #print(f"directory: {directory}")
    #print(f"files: {files}")
    for each_file in files:
        file_path = os.path.join(root,each_file)
        os.remove(file_path)

    for each_dir in directory:
        dir_path=os.path.join(root,each_dir)
        shutil.rmtree(dir_path)


#so all files are gone. only directory remains.

dir_test ='files'
for item in os.listdir(dir_test):
    print(item)





