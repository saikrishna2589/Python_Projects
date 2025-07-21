import pandas as pd
import os
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
import streamlit as st


#directory location
directory_loc = 'files/road_accidents_india'


#list files in dir
file_list = os.listdir(directory_loc)
print(file_list)


file_loc =os.path.basename(f"{file_list[0]}")

#construct file path
file_path_needed = os.path.join(directory_loc,file_loc)


#read data
df= pd.read_csv(file_path_needed)
print(df.head())

#cleansing data by dropping NA rows
print("Before dropping NA",len(df))
df_cleansed = df.dropna(subset=['latitude', 'longitude'])
print("After dropping NA", len(df_cleansed))

#initiate map object
mean_lat= df['latitude'].mean()
mean_lon = df['longitude'].mean()

print(mean_lat)
print(mean_lon)
map_object_india_accidents = folium.Map(location=[22.083748879753607,78.09848315869228], zoom_start=5)


#intiate the cluster
cluster_accidents = MarkerCluster()

#assign the datapoints as markers to the initiated map
for i, row in df_cleansed.iterrows():
    lat = row['latitude']
    lon = row['longitude']
    folium.CircleMarker(location=[lat,lon],
                  tooltip=row['Number_of_Casualties'],
                  color = 'crimson',
                  fill = 'crimson',
                 radius = row['Number_of_Casualties']*2
                  ).add_to(cluster_accidents)


#assign the cluster to the initiated map
cluster_accidents.add_to(map_object_india_accidents)

#save the map object to run on local html browser
#map_object_india_accidents.save('road_accidents.html')

#connecting folium map to streamlit web app
st_app = st_folium(map_object_india_accidents,width=1200, height=600)