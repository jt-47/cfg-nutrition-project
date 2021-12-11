from os import DirEntry
from PIL import Image
from flask import Flask, render_template, request, url_for
# import pandas as pd  
import requests
import json
from jinja2 import Environment, FileSystemLoader
from requests.api import get
import templates
from werkzeug.utils import redirect
from werkzeug.wrappers import response
import urllib.request
import csv
# import error_handling



app = Flask(__name__)

class CallAPI:

    def __init__(self,ingredient,health,diet,exclude) -> None:
        super().__init__()
        self.ingredient = ingredient
        self.health = health
        self.diet = diet
        self.exclude = exclude

@app.route("/", methods=['GET','POST']) 
def home():
    if request.method == 'GET':  #GET request is sent first to get web browser
        return render_template("index.html") 
    if request.method=='POST': #POST request to send the input info
        if 'usersfood' and 'userdietary' and 'userhealth' and 'userexclusion' in request.form:
           
            ingredient=request.form["usersfood"].lower()
            diet=request.form['userdietary'].lower()
            health=request.form['userhealth'].lower()
            exclude=request.form['userexclusion'].lower()
            print(ingredient)
            print(diet)
            print(health)
            print(exclude)
            hits = call_api()
        return render_template('recipes.html',hits=hits)
    


    

def call_api(): # Gets response from api
    ingredient=request.form["usersfood"].lower()
    diet=request.form['userdietary'].lower()
    health=request.form['userhealth'].lower()
    exclude=request.form['userexclusion'].lower()
    API_ID = "71b68ced"
    API_KEY = "e23ca4a79da18cff7d516f5e539033e4"
    response = requests.get(f'https://api.edamam.com/api/recipes/v2?type=public&beta=true&q={ingredient}&app_id={API_ID}&app_key={API_KEY}&diet={diet}&health={health}&time=10&imageSize=REGULAR&excluded={exclude}')
    r= response.json()
    hits=r['hits']
    return hits
             
## return the template with info as query strings. request.query[] ingred=ingred&diet=diet&health=health&​​

def list_recipe(ingredient,health,diet,exclude): # currently not showing in terminal

    recipe_info=[]
    hits = call_api()
    r =  call_api()
    info= call_api(ingredient,health,diet,exclude)

    for i in range(20):
        recipe = dict()
        recipe["recipe_name"]=hits[i]['recipe']['label']
        recipe["image"] = r["hits"][i]["recipe"]["image"]
        recipe["recipe_ingredients"] = r["hits"][i]["recipe"]["ingredients"]
        recipe["calories"] = r["hits"][i]["recipe"]["calories"]
        recipe["Energy"] = r["hits"][i]["recipe"]['totalNutrients']['ENERC_KCAL']
        recipe["Fat"] = r["hits"][i]["recipe"]['totalNutrients']['FAT']
        recipe["Sugar"] = r["hits"][i]["recipe"]['totalNutrients']['SUGAR']
        recipe["Protein"] = r["hits"][i]["recipe"]['totalNutrients']['PROCNT']
        recipe["Vitamn C"] = r["hits"][i]["recipe"]['totalNutrients']['VITC']
        recipe["allergies"] = r["hits"][i]["recipe"]['cautions']
        recipe["link"] = r["hits"][i]["recipe"]['url']
        
        
        recipe_info.append(recipe)
        print(recipe)
        return recipe



if __name__== "__main__":
    app.run(debug=True)

