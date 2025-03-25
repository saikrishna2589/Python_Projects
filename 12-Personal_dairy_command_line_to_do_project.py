#create dairy command line based program where users can store notes about their day
from datetime import datetime

notes_list =[]

while True:
    user_notes_input = input("Enter your notes for today. Type 'exit' to save and exit: ")
    if user_notes_input == 'exit':
        break
    notes_list.append(user_notes_input)


# filename build
day_today = datetime.now().strftime('%A')
filename = f"{day_today}.txt"

#convert list to string
string_notes = "\n".join(notes_list)

#createfile
with open(filename,'w') as file:
    file.write(string_notes)

print(f"Your notes have been saved to {filename}")
