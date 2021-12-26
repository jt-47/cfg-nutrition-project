import requests
import pandas as pd
#check this

#from collections import defaultdict
# self.user_info = defaultdict(list)
#self.user_info["recipe"].append(recipe)
#self.user_info["review"].append(review)

# Input queries
query = "chicken"  #input("What is your ingredient of choice?\n")

print("\nHere is a list of diet options: \n")
diet_list = ["balanced", "high-fiber", "high-protein", "low-carb", "low-fat", "low-sodium"]
for i in range(len(diet_list)):
    print(f'{i}. {diet_list[i]}')

diet = "high-fiber" #input("\nWhat is your diet choice?\n")
print("\nHere is a list of health options: \n")

health_list = ["alcohol-cocktail", "alcohol-free", "celery-free", "crustacean-free", "dairy-free", "DASH", "egg-free", "fish-free" "fodmap-free", "gluten-free", "immuno-supportive", "keto-friendly", "kidney-friendly", "kosher", "low-fat-abs", "low-potassium", "low-sugar", "lupine-free", "Mediterranean", "mollusk-free", "mustard-free", "no-oil-added", "paleo", "peanut-free", "pescatarian", "pork-free", "red-meat-free", "sesame-free", "shellfish-free", "soy-free", "sugar-conscious", "sulfite-free", "tree-nut-free", "vegan", "vegetarian", "wheat-free"]

for i in range(len(health_list)):
    print(f'{i}. {health_list[i]}')

health = "dairy-free" #input("\nWhat is your health choice?\n")


excluded = "tomato" #input("\nWhat are you allergic to??\n")

# Get the  response
response = requests.get(f'https://api.edamam.com/api/recipes/v2?q={query}&app_key=%203a045b9095af03671e2b052783e9e68a%09&_cont=CHcVQBtNNQphDmgVQntAEX4BYldtBAAFS2xJBmAbZlVwAAIAUXlSAGEVNQMiBApRRDZGV2AQZAF0UQIPSmJIVmoaawZ6AFEVLnlSVSBMPkd5BgMbUSYRVTdgMgksRlpSAAcRXTVGcV84SU4%3D&type=public&app_id=9bda37b4&diet={diet}&health={health}&excluded={excluded}').json()

print("-----------")
# print(response) #how to access the ["hits"][0]["recipe"]
print("-----------")
# print(response["hits"][0]["recipe"].keys()) #all the keys to choose from

# see the recipes
recipe_info = [] #[{}, {}, {}]
for i in range(20): #20 recipes
    recipe = dict()
    recipe["number"] = i
    recipe["recipe_name"] = response["hits"][i]["recipe"]["label"] #dict[key] = value
    recipe["image"] = response["hits"][i]["recipe"]["image"]
    recipe["recipe_ingredients"] = response["hits"][i]["recipe"]["ingredientLines"]
    recipe["calories"] = response["hits"][i]["recipe"]["calories"]
    recipe["total_nutrients"] = response["hits"][i]["recipe"]['totalNutrients']
    recipe["allergies"] = response["hits"][i]["recipe"]['cautions']

    recipe_info.append(recipe)
    print(recipe)

# check if the ingredients are in the recipe
ingredients_list = [] #list of strings
for i in range(20): #10 recipes
   ingredients_string = "".join(response["hits"][i]["recipe"]["ingredientLines"])
   ingredients_list.append(ingredients_string)

# for i in ingredients_list:
#     if "chicken" in i and "lemon" in i and "parsley" in i:
#         print("true")

for i in ingredients_list:
    if "cheese" in i:
        print("true")
    else:
        print("false")

#see the info in a table using pandas

# df = pd.DataFrame(recipe_info)
# print(df)
#
# print(df.columns)
#
# print(df.iloc[0])
# print(df.iloc[0, 2])

# print(len(response["hits"])) #never get more than 20 recipes as we are getting the free version