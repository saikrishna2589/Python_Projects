from flask import Flask,render_template
import requests


api_key ='4ab757abe0f042728570a4cfce6d64dc'
url= f"https://newsapi.org/v2/top-headlines?apiKey={api_key}&q=business"

app = Flask(__name__)

@app.route('/')
#function responsbile to render what to show to the users
def home():
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    return render_template('index.html',our_articles = articles )

if __name__ == "__main__":
    app.run(debug=True)



