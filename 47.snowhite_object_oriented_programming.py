import os

class Input_output:
    #provide filepath
    def __init__(self,file_path):
        self.file_path = file_path

#method to read the file_path
    def read(self):
        with open(self.file_path,'r') as file:
            input_data = file.read()
            return input_data

    def write(self,content):
        file = os.path.basename(self.file_path)
        output_file_name = os.path.join(os.curdir,f"sentence_capitalised_{file}")
        with open(output_file_name,'w') as file:
            file.write(content)



class Sentence_caps():
    def __init__(self,data):
             self.data = data

    def data_to_cap(self):
        # Split the text into sentences and capitalize the first letter of each sentence
        sentences = self.data.split(". ")

        corrected_sentences = []

        for sentence in sentences:
            corrected_sentences.append(sentence.capitalize())
        corrected_text = ". ".join(corrected_sentences)
        return corrected_text


input_file =Input_output('snowwhite.txt')

read_file = input_file.read()

sentences_to_caps =Sentence_caps(read_file)

first_word_caps =sentences_to_caps.data_to_cap()

input_file.write(first_word_caps)





