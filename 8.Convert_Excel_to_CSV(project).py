import pandas as pd

df = pd.read_excel('europe.xlsx')

print(df)

df_to_csv = df.to_csv('europe.csv' ,header = True , index=False )