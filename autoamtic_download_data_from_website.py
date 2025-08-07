#step 1 -->input
# url
import requests

url= 'https://www.ncei.noaa.gov/pub/data/ghcn/daily/by_year/'

#you want filepath and files save with data using tha filepath
#so if you select 1900 year, then 1900.csv.gz is the filepath

#step 2: construct filepath
def construct_filepath(year):
    filepath = f"{year}.csv.gz"
    return filepath


#step 3 - create new file with this filepath
def write_to_file(filepath,content):
    with open(filepath,'wb') as file:
        file.write(content)




#step3-->
#define function that download data for one file.
#i.e if you want files for year 2000-2005, write function to download for one year.

def url_year(url,filepath):
    file_url = f"{url}{filepath}"
    return file_url

#step 4-->
#write a for loop and calls this function 5 times here i.e year in range(2000,2005)
for each_year in range(1900, 1903):
    file_path =construct_filepath(each_year) #1768.csv.gz
    file_url = url_year(url,file_path)  #fullurl https://www.ncei.noaa.gov/pub/data/ghcn/daily/by_year/1768.csv.gz
    response = requests.get(file_url).content
    write_to_file(file_path,response)


