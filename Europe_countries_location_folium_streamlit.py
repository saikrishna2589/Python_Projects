import pandas as pd
import streamlit as st
import folium
from numba.np.numpy_support import map_layout
from streamlit_folium import st_folium

data = 'files/europe.csv'


st.set_page_config(layout='wide')
st.title('Europe Countries Location')
#convert data to df
df = pd.read_csv(data)
#create a folium map object (layout)

map_initial = folium.Map(location=
                         [df['Latitude'].mean(),
                         df['Longitude'].mean()],
                         zoom_start=2)

#assign the Country locations to the map

for i, row in df.iterrows():
    lat = row['Latitude']
    lon =row ['Longitude']
    (folium.Marker(location= [lat,lon],
                   color='crimson',
                   fill='crimson',
                   tooltip= f"Loc : {row['Country']}")
     .add_to(map_initial))


#map_initial.save('europe_map.html')

#open on local host instead of local drive so you can share the url to others as well.
st_folium(map_initial,width=1200)
