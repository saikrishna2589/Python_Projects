import pandas as pd
import folium
from folium.plugins import  MarkerCluster

#load the dataset
data = 'files/accidents.csv'
df = pd.read_csv(data, sep=';')
print(df.head())


#folium map initiate
mean_lat = df['LATITUDE'].mean()
mean_long = df['LONGITUD'].mean()
map_object = folium.Map(location=[mean_lat,mean_long],zoom_start=4)


#initiate cluster
cluster = MarkerCluster()


#connect the datapoints to the map
for i, row in df.iterrows():
    lat = row['LATITUDE']
    lon = row['LONGITUD']
    folium.Marker(location=[lat,lon],
                  tooltip=row['MAN_COLLNAME']).add_to(cluster)


#adding cluster with datapoints to the initated map
cluster.add_to(map_object)
#save in local html browser
map_object.save('accident_map.html')


