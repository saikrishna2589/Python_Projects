import flask
#Flask is a webframework. It is used to build webapps and RestApis

from flask import Flask
import json
#create an Flask app instance
app = Flask(__name__)

#store books.json in the python dictionary

with open('files/books.json') as file_object:
    books_dictionary = json.load(file_object)


#now we use flask to help[ with creating the webip
#we provide endpoints format needs to be adhered by the user
#user would then be returned the data based on endpoint api


#app.route decorator to define endpoints
# Define an API endpoint to retrieve book information based on book_id
@app.route('/books_info/<book_id>')
def book_api_endpoint(book_id):
     book_info = books_dictionary.get(book_id)
     if book_info:
         return book_info
     else:
         return {'message':'Book_id not found'}, 404


@app.route('/')
def homepage():
    return books_dictionary


#Run the Flask app explicitly

if __name__ =='__main__':
    app.run(debug= True)  #debug=True is helpful during development