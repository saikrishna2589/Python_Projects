import requests
import pandas as pd

def get_raw_data(startdate, enddate):
    url ='https://earthquake.usgs.gov/fdsnws/event/1/query'
    params ={'format' : 'geojson',
             'starttime': startdate,
             'endtime' : enddate
             }
    response = requests.get(url, params=params)
    print(response)
    data = response.json()
    return data


def clean_data(raw_data):
    extracted_data = []
    for feature in raw_data['features']:
        extracted_dict = {'Magnitude': feature['properties']['mag'] ,
                          'place': feature['properties']['place'] ,
                           'latitude': feature['geometry']['coordinates'][1],
                          'longitude': feature['geometry']['coordinates'][0],}
        extracted_data.append(extracted_dict)
    return extracted_data


#export to csv

def export_to_csv(cleansed_final_data,path):
    final_data = pd.DataFrame(cleansed_final_data)
    final_data.to_csv(path, index=False )

data_ingested = get_raw_data('2015-01-01' ,'2015-01-02')
cleansed_data = clean_data(data_ingested)
export_to_csv(cleansed_data, 'files/export_cleanesed_Earthquakedata.csv' )


