import os  # Import os to work with file paths

# Declare a class for file input/output operations
class Input_output_filepath:
    def __init__(self, file_path):
        self.file_path = file_path  # Save the file path

    # Method to read content from the file
    def read(self):
        with open(self.file_path, 'r') as file:  # Open file in read mode
            data = file.read()  # Read the entire content as a string
            return data  # Return the string data

    # Method to write data to a new file
    def write(self, input):
        # Extract folder and file name to avoid path issues
        folder = os.path.dirname(self.file_path)  # e.g., 'files'
        filename = os.path.basename(self.file_path)  # e.g., 'content_to_reverse_words'

        # Create new file path: files/reversed_content_to_reverse_words
        new_file_path = os.path.join(folder, f"reversed_{filename}")

        # Open the new file in write mode and save the reversed content
        with open(new_file_path, 'w') as file:
            file.write(input)


# Class to reverse each word in a sentence
class Reversed:
    def __init__(self, input_text):
        self.input_text = input_text  # Save the original input string

    def reversed_words(self):
        data_input = self.input_text.split()  # Split input into words by spaces

        reversed_word_list = []  # Empty list to hold reversed words

        for word in data_input:
            data_input_reversed = word[::-1]  # Reverse the characters of each word
            reversed_word_list.append(data_input_reversed)  # Add to list

        reversed_sentence = " ".join(reversed_word_list)  # Join all reversed words with space
        return reversed_sentence  # Return the final reversed sentence


# -------- Main program flow --------

# Create an object to handle file reading and writing
file_path = Input_output_filepath('files/content_to_reverse_words')

# Read the content of the file
data_to_reverse = file_path.read()

# Create an object to reverse the words in the text
data_to_reverse_store = Reversed(data_to_reverse)

# Call method to get text with each word reversed
reversed_data = data_to_reverse_store.reversed_words()

# Write the reversed text to a new file
file_path.write(reversed_data)
