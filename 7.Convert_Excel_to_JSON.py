#when thinking about processing excel files, think of pandas library
import pandas as pd

df = pd.read_excel('europe.xlsx')


convert_to_json_df = df.to_json('europe.json')

#another variation in format
#orientation ='records' would make each row one dictionary.
#leaving  lines= False ,which is default, will make it list of dictionaries.
#if you want only dictionaries each one to itself and no list, then #Lines=True

#check file formats for seeing both the files differences
convert_to_json_variation_df = df.to_json('europe_format.json' ,orient = 'records' ,lines =True)
