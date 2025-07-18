import pandas as pd
import plotly.express as px  # 2 sub-modules.
#express shortens the lines.


file = 'files/houses.csv'

data = pd.read_csv(file)

#plotly
fig=px.scatter(data,x='Size',y='Price',color='Location' ,
               title='House Price vs. Size',
               hover_data={'Bedrooms':True,
                           'Bathrooms':True,
                           'Age':True,
                           'Size':False})

fig.show()