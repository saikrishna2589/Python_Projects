import requests

api_Key = 'xxxx'  # Make sure to keep this secret in production

def news_api_extract(topic):
    url = "https://newsapi.org/v2/top-headlines"

    response = requests.get(
        url,
        params={
            'category': topic,
            'apiKey': api_Key,
            'country': 'us'  # optional but recommended
        }
    )

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None



# Extract required data

def required_data(news):
    data = news['articles']
    data_extract =  []
    for i,each in enumerate(data):
        data_extract.append({
            f'title_{i}':each.get('title'),
            f'description_{i} ':each.get('description'),
            f'publishedAt_{i} ': each.get('publishedAt'),
            f'url_{i} ': each.get('url')
             })

    return  data_extract

    #i want to loop list of dict and extract title ,desc,#url.

extract_news = news_api_extract('business')
data_extracted =required_data(extract_news)




