
#write a to-do-list program that saves the to-do list daily
#write it to a file .
# #Name the file the current day of the week

from datetime import datetime
to_do_list= []
while True:
    user_entry = input("Enter your to-do task.  Press 'done' once complete: ")
    if user_entry == 'done':
        break
    to_do_list.append(user_entry)

print(to_do_list)

#constructing the filename
today =  datetime.now().strftime('%A')

filename = f"{today}.txt"

#convert list to a string

to_do_list_string = "\n".join(to_do_list)
print(to_do_list_string)

with open(filename,'w') as file:
    to_do_file = file.write(to_do_list_string)


print(f"your to-do list file is created and can be viewed here : {filename}")





