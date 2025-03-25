recipes = {
    1: {'id': 1, 'title': 'Spaghetti Carbonara', 'ingredients': ['spaghetti', 'eggs', 'pecorino cheese', 'guanciale'], 'instructions': 'Cook pasta, fry guanciale, mix with eggs and cheese, and combine with pasta.'},
    2: {'id': 2, 'title': 'Tomato Soup', 'ingredients': ['tomato', 'water', 'salt'], 'instructions': 'Boil all together until mushy, blend, and serve.'},
    3: {'id': 3, 'title': 'Grilled Cheese Sandwich', 'ingredients': ['bread', 'cheese', 'butter'], 'instructions': 'Butter bread, place cheese between slices, grill until golden.'}
}

#what to do now?

#i want to show to the user in restapi format the recipies they are after.
#i have data in dictionary format.

#so no need to read data with open() method and json.load() as data is already in dict format.

#import flask class from flask library
from flask import Flask , jsonify

#create flask app instance
app = Flask(__name__)

#define the restapi endpoints
@app.route('/recipie/<int:recipie_id>',methods = ['GET'])
def recipie_data(recipie_id):
    recipe_requested = recipes.get(recipie_id)
#using the get method to get the
    if recipe_requested:
        return jsonify(recipe_requested)
    else:
        return  jsonify({'message':f"{recipie_id} doesn't exist"},404)


@app.route('/')
def homepage():
    return "Homepage"

#run app explicitly
if __name__=='__main__':
    app.run(debug=True)

