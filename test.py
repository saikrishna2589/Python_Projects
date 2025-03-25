import os
import time
from datetime import datetime

current_file_directory = 'files'

# Get a list of filenames in the directory
current_file_names = os.listdir(current_file_directory)

for filename in current_file_names:
    current_file_path = os.path.join(current_file_directory, filename)

    # Read the file content
    with open(current_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Ensure file is closed before renaming
    time.sleep(0.5)  # Small delay to allow OS to release file lock

    # Count words
    words = content.split()
    word_count = len(words)

    # Get current day
    current_day = datetime.now().strftime("%A")

    # Construct new filename
    file_base_name, file_extension = os.path.splitext(filename)
    new_file_name = f"{file_base_name}-{word_count}-{current_day}{file_extension}"
    new_file_path = os.path.join(current_file_directory, new_file_name)

    # Rename file
    try:
        os.rename(current_file_path, new_file_path)
        print(f"Renamed: {filename} -> {new_file_name}")
    except PermissionError:
        print(f"⚠️ PermissionError: Unable to rename {filename}. File might be in use.")
