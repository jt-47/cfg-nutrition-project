from os import DirEntry
from PIL import Image
from flask import Flask, render_template, request, url_for
from flask.helpers import flash
# import pandas as pd  
import requests
import json
from jinja2 import Environment, FileSystemLoader
from requests import api
from requests.api import get
import templates
from werkzeug.utils import redirect
from werkzeug.wrappers import response
import csv
import requests
import pandas as pd

class CallAPI:

    app_id = "9bda37b4"
    app_key = "3a045b9095af03671e2b052783e9e68a"
    recipe_info = []
    response = None
    recipe_table = None

    def __init__(self, ingredient, health, diet, exclude):
        self.ingredient = ingredient
        self.health = health
        self.diet = diet
        self.exclude = exclude
        self.database = []

    def call_api(self):
        self.response = requests.get(f'https://api.edamam.com/api/recipes/v2?q={self.ingredient}&app_key=%20{self.app_key}%09&_cont=CHcVQBtNNQphDmgVQntAEX4BYldtBAAFS2xJBmAbZlVwAAIAUXlSAGEVNQMiBApRRDZGV2AQZAF0UQIPSmJIVmoaawZ6AFEVLnlSVSBMPkd5BgMbUSYRVTdgMgksRlpSAAcRXTVGcV84SU4%3D&type=public&app_id={self.app_id}&diet={self.diet}&health={self.health}&excluded={self.exclude}')
        
        r = self.response.json()

        for item in range(20):
            hits=r['hits']
        return hits
        
    def get_recipe_info(self):

        for i in range(20):
            recipe = dict()

            recipe["recipe_name"] = self.response["hits"][i]["recipe"]["label"]
            recipe["image"] = self.response["hits"][i]["recipe"]["image"]
            recipe["recipe_ingredients"] = self.response["hits"][i]["recipe"]["ingredientLines"]
            recipe["calories"] = round(self.response["hits"][i]["recipe"]["calories"], 2)
            recipe["total_nutrients"] = self.response["hits"][i]["recipe"]['totalNutrients']
            recipe["allergies"] = self.response["hits"][i]["recipe"]['cautions']

            self.recipe_info.append(recipe)


    def check_ingredient(self, *args):
        '''
              This is a method for the developer to check if the ingredients are present in the recipe.
              It is not really for the user to use hence it does not need to be in the main class.
          '''

        ingredients_list = []
        for i in range(len(self.recipe_info)):
            ingredients_string = "".join(self.response["hits"][i]["recipe"]["ingredientLines"])
            ingredients_list.append(ingredients_string)

        for a in args:
            for i in ingredients_list:
                if a in i:
                    print("true")
                else:
                    print("false")

    def new_decorator(func):
        def wrap_func(self):
            print("------------------------------------------------------------------------------------------")
            func(self)
            print("-------------------------------------------------------------------------------------------")

        return wrap_func

    @new_decorator #database
    def ask_user(self):
        recipe = self.recipe_info[int(input("What recipe would you like to review?\n"))-1]["recipe_name"]
        review = input("Please input your review:\n ")

        while True:
            try:
                rating = int(input("\nPlease input your rating from 1 to 5:\n"))
            except:
                print("\nYou should only put in numbers, please try again:\n ")
            else:
                if rating < 6:
                    break

        recipe_list = [i[0] for i in self.database]
        if recipe not in recipe_list:
            self.database.append([recipe, review, rating])
        else:
            recipe_index = recipe_list.index(recipe)
            self.database[recipe_index] = [recipe, review, rating]
        pd.DataFrame(self.database, columns=["Recipe name", "Review", "Rating"]).to_csv("database.csv", index=False)
