from os import DirEntry
from PIL import Image
from flask import Flask, render_template, request, url_for
import pandas as pd  
import requests
import json
from jinja2 import Environment, FileSystemLoader
from requests import api
from requests.api import get
import templates
from werkzeug.utils import redirect
from werkzeug.wrappers import response
import urllib.request
import csv
# import error_handling



app = Flask(__name__)

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
            hits = call_api()
        return render_template('recipes.html',hits=hits)
    
def call_api(): # Gets response from api
    ingredient=request.form["usersfood"].lower()
    diet=request.form['userdietary'].lower()
    health=request.form['userhealth'].lower()
    exclude=request.form['userexclusion'].lower()
    recipe_infor=[]
    API_ID = "71b68ced"
    API_KEY = "e23ca4a79da18cff7d516f5e539033e4"
    response = requests.get(f'https://api.edamam.com/api/recipes/v2?type=public&beta=true&q={ingredient}&app_id={API_ID}&app_key={API_KEY}&diet={diet}&health={health}&time=10&imageSize=REGULAR&excluded={exclude}')
    r= response.json()
    hits=r['hits']
    recipe_infor.append(hits)
    df = pd.DataFrame.from_dict(recipe_infor)
    df.to_csv (r'gen.csv', index = False, header=True)
    return hits




        

                

if __name__== "__main__":
    app.run(debug=True)