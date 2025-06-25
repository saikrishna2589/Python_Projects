

import pandas as pd
from io import StringIO

#file_name = 'europe.xlsx'

def excel_to_csv(filename):
    user_file = pd.read_excel(filename)
    convert_to_csv = user_file.to_csv(index=False,sep =',')
    return convert_to_csv


