import matplotlib.pyplot as plt
import os
import glob

directory ='files/matplotlib_project'

file_path = glob.glob(f'{directory}/*.txt')

print(file_path)

data_read_store=[]

for filepath in file_path:
    with open(filepath,'r') as file:
        data = file.read()
        data = float(data.strip())
        data_read_store.append(data)

print(data_read_store)
print(type(data_read_store))

#obtaining the filenames
file_name_list =[]

for file in file_path:
    file_name = os.path.basename(file)
    file_name = file_name.strip('.txt')
    file_name = file_name[0]
    file_name_list.append(file_name)


print(file_name_list)
print(data_read_store)

plt.figure(figsize=(8,6))

plt.plot(file_name_list,data_read_store,marker='o',color='r')

plt.xlabel('file_name')
plt.xticks(rotation=45)
plt.ylabel('values')
plt.tight_layout()
plt.title('values over filename')
plt.grid(True)


plt.show()