import glob

# Set the directory where your input files are located
file_dir = 'inputs'

# Use glob to get a sorted list of all .txt files in the directory
filepath_list = sorted(glob.glob(f'{file_dir}/*.txt'))

# Create an empty list to store contents of all files
contents_merged_list = []

# Loop through each file path
for file_path in filepath_list:
    # Open each file in read mode
    with open(file_path, 'r') as file_object:
        # Read entire content of the file
        file_content = file_object.read()
        # Append the content to the list
        contents_merged_list.append(file_content)

# After collecting all contents, open output file once in write mode
with open('inputs/merged_file.txt', 'w') as file_output:
    # Loop through all stored contents
    for content in contents_merged_list:
        # Write each content to the merged file, adding newline after each
        file_output.write(content + '\n')
