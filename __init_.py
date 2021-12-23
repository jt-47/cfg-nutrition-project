
from os import DirEntry
from PIL import Image
from flask import Flask, render_template, request, url_for
from flask.helpers import flash
import pandas as pd  
import requests
import json
from jinja2 import Environment, FileSystemLoader
from requests import api
from requests.api import get
import templates
from werkzeug.utils import redirect
from werkzeug.wrappers import response
import csv
from CALL_API import CallAPI
app = Flask(__name__)

class Run:


    def __init__(self, ingredient, health, diet, exclude):
        self.ingredient = ingredient
        self.health = health
        self.diet = diet
        self.exclude = exclude
        # self.database = []

    @app.route("/", methods=['GET','POST']) 
    @app.route("/recipes", methods=['GET','POST'])
    def home():

        if request.method == 'GET':  #GET request is sent first to get web browser
            return render_template("index.html") 

        if request.method=='POST': #POST request to send the input info
            if 'usersfood' and 'userdietary' and 'userhealth' and 'userexclusion' in request.form:
                
                ingredient=request.form["usersfood"].lower()
                diet=request.form['userdietary'].lower()
                health=request.form['userhealth'].lower()
                exclude=request.form['userexclusion'].lower()
                # ca=CallAPI(ingredient,diet,health,exclude)
                # # rc=ca.get_recipe_info()
                # # print(ingredient)
                ca=Run
                hits = ca.call_api()
                return render_template('recipes.html',hits=hits)


    @app.route("/recipes/add", methods=['POST'])
    def ratings():
        if request.method == 'POST':
            if 'rating' and 'review' and 'name' and 'recipe' in request.form:
                rating=request.form["rating"]
                review=request.form["review"]
                name=request.form["name"]
                recipe=request.form["recipe"]
            
                
                create_row_data = {
                'name': str(name), 
                'recipe': str(recipe), 
                'rating': str(rating), 
                'review': str(review)
                    }
                rating_table = pd.DataFrame(create_row_data,index=[0])
                rating_table.to_csv('recipe_ratings.csv', index=False)
                read_ratings=pd.read_csv('recipe_ratings.csv')
                read_ratings.to_html('ratings.html')
                return render_template('ratings.html')

        

    def call_api(): # Gets response from api
        ingredient=request.form["usersfood"].lower()
        diet=request.form['userdietary'].lower()
        health=request.form['userhealth'].lower()
        exclude=request.form['userexclusion'].lower()
        ca=Run
        ca.home
        API_ID = "71b68ced"
        API_KEY = "e23ca4a79da18cff7d516f5e539033e4"

            
        response = requests.get(f'https://api.edamam.com/api/recipes/v2?type=public&beta=true&q={ingredient}&app_id={API_ID}&app_key={API_KEY}&diet={diet}&health={health}&time=10&imageSize=REGULAR&excluded={exclude}')

        try:
            if response.status_code == 200:
                r = response.json()
            elif response.status_code != 200:
                print ("bad status code")
        except Exception as e:
            raise

        hits=r['hits']
        return hits

    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def not_found_error(error):
        return render_template('500.html'), 500   
# ca=Run
# hits = ca.call_api     

if __name__== "__main__":
    app.run(debug=True)  #Remove the Debug=True when the flask app is finished to see the 500 error page