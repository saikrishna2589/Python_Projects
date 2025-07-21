import streamlit as st
import folium
import streamlit_folium
import pandas as pd
earth_quake_data = 'files/export_cleanesed_Earthquakedata.csv'
from streamlit_folium import st_folium


#2 parts to this app
#1st part extracting json data and cleansing in part of code to get the above data
#2nd part is to load this in web map format in streamlit using folium library
#convert to df using pandas df

st.set_page_config(layout='wide')
st.title('Earthquake Global Map')


data =pd.read_csv(earth_quake_data)
print(data.head())

#calculating the mean for latitude and longitude to get center of all datapoints for the folium map.
#this data point will be the initial load when map loads.

mean_lat = data['latitude'].mean()

mean_lon = data['longitude'].mean()


map_startpoint = folium.Map(location=[mean_lat, mean_lon] , zoom_start=2)

#adding location of earthquake to the map provided by folium.

for i,row in data.iterrows():
    lat =row['latitude']
    long = row['longitude']

    (folium.CircleMarker
     (location=[lat,long],
      radius = row['Magnitude']*2,
      color = 'crimson',
      fill=True,
      fill_color ='crimson',
      tooltip =f"Loc : {row['place']} \n "
              f"Mag : {row['Magnitude']}")
     .add_to(map_startpoint))

#open as html on local browser
#map_startpoint.save('map.html')

#open using local host url so others can access as well

st_folium(map_startpoint,width=1200)






