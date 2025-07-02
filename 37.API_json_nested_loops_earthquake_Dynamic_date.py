import requests
import pandas as pd
import datetime as dt


yesterday_date = dt.date.today() - dt.timedelta(days=1)

yesterday_date = dt.date.strftime(yesterday_date , "%Y-%m-%d")



def get_raw_data(startdate = yesterday_date, enddate=yesterday_date):
    url ='https://earthquake.usgs.gov/fdsnws/event/1/query'
    params ={'format' : 'geojson',
             'starttime' :startdate,
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
                          'Location': feature['properties']['place'] ,
                           'latitude': feature['geometry']['coordinates'][1],
                          'longitude': feature['geometry']['coordinates'][0],}
        extracted_data.append(extracted_dict)
    return extracted_data


#export to csv

def export_to_csv(cleansed_final_data,path):
    final_data = pd.DataFrame(cleansed_final_data)
    final_data.to_csv(path, index=False )

data_ingested = get_raw_data( )
cleansed_data = clean_data(data_ingested)
export_to_csv(cleansed_data, f'files/export_cleanesed_Earthquakedata_{yesterday_date}.csv' )


