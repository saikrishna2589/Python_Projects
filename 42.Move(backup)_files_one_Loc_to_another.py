import os
import shutil
import datetime as dt

# Step 1: Check if the "Backup" folder exists in current working directory
# If it does, print a message; if not, create it
if os.path.exists('Backup'):
    print("Folder exists")
else:
    os.mkdir('Backup')  # Creates a new folder named "Backup"

# Step 2: Create a new subfolder inside "Backup" with a timestamp as its name
# This helps you organize backups by time and avoid overwriting
current_datetime = dt.datetime.now().strftime("%Y%m%d%H%M%S")  # Format: YYYYMMDDHHMMSS
backup_sub_folder = os.path.join('Backup', current_datetime)  # Full path to new subfolder

os.mkdir(backup_sub_folder)  # Actually create the subfolder
print(backup_sub_folder)  # Print path for confirmation/logging

# Step 3: Define the source directory (your fake Downloads folder)
copy_from_path = 'Downloads_test'  # This is the folder you want to back up

# Step 4: Move every file/folder from Downloads_test to the new backup folder
for item in os.listdir(copy_from_path):  # Loop through everything in Downloads_test
    file_path = os.path.join(copy_from_path, item)  # Full path of each file/folder
    shutil.move(file_path, backup_sub_folder)  # Move file/folder to backup location
    print(f"{item} has been moved successfully to {backup_sub_folder}")  # Confirmation message
