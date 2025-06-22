import pandas as pd

def excel_to_json(excel_file_path):
    input_data = pd.read_excel(excel_file_path)  #read the excel file
    json_convert = input_data.to_json(
        orient='records')   #convert to json
    return json_convert



