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
import csv
import error_handling



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
    API_ID = "71b68ced"
    API_KEY = "e23ca4a79da18cff7d516f5e539033e4"
    response = requests.get(f'https://api.edamam.com/api/recipes/v2?type=public&beta=true&q={ingredient}&app_id={API_ID}&app_key={API_KEY}&diet={diet}&health={health}&time=10&imageSize=REGULAR&excluded={exclude}')
    r= response.json()
    hits=r['hits']
    return hits

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def not_found_error(error):
    return render_template('500.html'), 500            

if __name__== "__main__":
    app.run(debug=True)