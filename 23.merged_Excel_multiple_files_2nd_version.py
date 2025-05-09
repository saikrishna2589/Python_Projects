import os
import pandas as pd  # Using pandas as pd is the standard convention


# Set the directory where Excel files are stored
directory_name = 'project_excel_files_data_merge'

# Get the list of all files in the directory
file_names = os.listdir(directory_name)

# Create a dictionary to categorize files by year
data_dictionary = {'2024': [], '2025': []}

# Loop through each file in the directory
for file in file_names:
    # Build full path for the current file
    file_path = os.path.join(directory_name, file)

    # Check if file is a 2024 Excel file
    if file.endswith('2024.xlsx'):
        # Read Excel file and append the DataFrame to the '2024' list
        df_2024 = pd.read_excel(file_path, engine='openpyxl', index_col=False)
        data_dictionary['2024'].append(df_2024)

    # Check if file is a 2025 Excel file
    elif file.endswith('2025.xlsx'):
        # Read Excel file and append the DataFrame to the '2025' list
        df_2025 = pd.read_excel(file_path, engine='openpyxl', index_col=False)
        data_dictionary['2025'].append(df_2025)

# Now we have a dictionary: each year maps to a list of DataFrames

# Merge all DataFrames for each year into a single DataFrame
for year in ['2024', '2025']:
    if data_dictionary[year]:  # Proceed only if there is data for the year
        # Concatenate list of DataFrames
        merged_df = pd.concat(data_dictionary[year], ignore_index=True)  # Use ignore_index=True for clean indexing
        output_path = f"{directory_name}/merged_df_{year}.xlsx"
        # Write merged DataFrame to Excel
        merged_df.to_excel(output_path, index=False)

# Read and display the merged 2024 data as a check
df = pd.read_excel(f"{directory_name}/merged_df_2024.xlsx")
print(df)
