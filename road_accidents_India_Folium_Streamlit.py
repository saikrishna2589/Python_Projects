import pandas as pd
import os
import folium
from folium.plugins import MarkerCluster
import streamlit as st  # ✅ You forgot this!
from streamlit_folium import st_folium

# App Title (must have at least one st command to render)
st.title("🚗 India Road Accident Map - Casualty Clusters")

# directory location
directory_loc = 'files/road_accidents_india'

# list files in dir
file_list = os.listdir(directory_loc)
print(file_list)

file_loc = os.path.basename(f"{file_list[0]}")

# construct file path
file_path_needed = os.path.join(directory_loc, file_loc)

# read data
df = pd.read_csv(file_path_needed, low_memory=False)
print(df.head())

# cleansing data by dropping NA rows
print("Before dropping NA", len(df))
df_cleansed = df.dropna(subset=['latitude', 'longitude'])
print("After dropping NA", len(df_cleansed))

# initiate map object
mean_lat = df_cleansed['latitude'].mean()
mean_lon = df_cleansed['longitude'].mean()

map_object_india_accidents = folium.Map(location=[mean_lat, mean_lon], zoom_start=5)

# initiate the cluster
cluster_accidents = MarkerCluster()

# assign the datapoints as markers to the initiated map
for i, row in df_cleansed.iterrows():
    lat = row['latitude']
    lon = row['longitude']
    folium.CircleMarker(
        location=[lat, lon],
        tooltip=row['Number_of_Casualties'],
        color='crimson',
        fill=True,
        fill_color='crimson',
        radius=row['Number_of_Casualties'] * 2
    ).add_to(cluster_accidents)

# assign the cluster to the initiated map
cluster_accidents.add_to(map_object_india_accidents)

# show map in Streamlit
st_folium(map_object_india_accidents, width=1200, height=600)
