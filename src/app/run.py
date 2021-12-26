from flask import Flask, render_template, request, url_for
# from flask.helpers import flash
import pandas as pd  
import requests
import json
from jinja2 import Environment, FileSystemLoader
from requests import api
from requests.api import get
import templates
from werkzeug.utils import format_string, redirect
from werkzeug.wrappers import response
import csv
from CALL_API import CallAPI
# from main import main


app = Flask(__name__)

"""GET and POST requests send to the server to send and retrieve data from the edamam api"""
@app.route("/", methods=['GET']) #Sends a GET request to the server to display the hompage (/)
@app.route("/recipes", methods=['GET','POST']) #POST request is sent to the server to accept the inputed data
def home():

    if request.method == 'GET':  #Sends a GET request to the server to display the hompage (/)
        return render_template("index.html")  
    try:
        if request.method=='POST': #POST request is sent to the server to accept the inputted data
            if 'usersfood' and 'userdietary' and 'userhealth' and 'userexclusion' in request.form:
                    
                query=request.form["usersfood"].lower()
                diet=request.form['userdietary'].lower()
                health=request.form['userhealth'].lower()
                excluded=request.form['userexclusion'].lower()
                api = CallAPI(query, health, diet, excluded)
                hits= (api.call_api())  # The inputted data is sent to the api method to retrieve the data
                
    except Exception as e:
        print ('An internal error has occurred',e)
        return render_template('500.html')
    
    return render_template('recipess.html',hits=hits)

"""User recipe rating"""
"""Aim was to call the database from the ask_user method and show it on the ratings.html page. 
However we encountered a few errors. The database is visable through the terminal folder"""

# @app.route("/recipes/add", methods=['POST']) #POST request sent to accept the user inputs
# def ratings():
    
#     if request.method == 'POST':
#         if 'recipe_num' and 'review' in request.form:
#             rating=request.form["rating"]
#             review=request.form["review"]
#             name=request.form["name"]
#             recipe=request.form["recipe"]
        
#             # ca=CallAPI(name,rating,review,name)
#             return render_template('ratings.html')



@app.route("/aboutus", methods=['GET'])
def about_us():
    return render_template('About Us.html')

@app.route("/contactus", methods=['GET'])
def contact_us():
    return render_template('Contact Us.html')

"""Error handlers to customise error pages"""

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def not_found_error(error):
    return render_template('500.html'), 500   


if __name__== "__main__":
    app.run()  #Remove the Debug=True when the flask app is finished to see the 500 error page