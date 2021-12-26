import requests
import pandas as pd

class CallAPI:

    app_id = "9bda37b4"
    app_key = "3a045b9095af03671e2b052783e9e68a"

    def __init__(self, username, query, health, diet, excluded):
        self.username = username
        self.query = query
        self.health = health
        self.diet = diet
        self.excluded = excluded
        self.database = []
        self.recipe_info = []
        self.response = None
        self.recipe_table = None

        self.df = pd.read_csv("database.csv", index_col=0)

        for i in range(self.df.shape[0]):
            self.database.append(list(self.df.iloc[i]))

    def call_api(self):
        self.response = requests.get(f'https://api.edamam.com/api/recipes/v2?q={self.query}&app_key=%20{self.app_key}%09&_cont=CHcVQBtNNQphDmgVQntAEX4BYldtBAAFS2xJBmAbZlVwAAIAUXlSAGEVNQMiBApRRDZGV2AQZAF0UQIPSmJIVmoaawZ6AFEVLnlSVSBMPkd5BgMbUSYRVTdgMgksRlpSAAcRXTVGcV84SU4%3D&type=public&app_id={self.app_id}&diet={self.diet}&health={self.health}&excluded={self.excluded}').json()

    def get_recipe_info(self):

        if self.response["hits"] == []:
            print("\nThere is no result for this query.\n")
            return

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
            return self.database
        return wrap_func

    @new_decorator
    def ask_user(self):

        while True:
            try:
                recipe_num = int(input("What recipe would you like to review?\n"))-1
            except:
                print("\nYou should only put in numbers within the range, please try again:\n")
            else:
                if recipe_num < 21:
                    break

        recipe = self.recipe_info[recipe_num]["recipe_name"]

        review = input("Please input your review:\n ")


        while True:
            try:
                rating = int(input("\nPlease input your rating from 1 to 5:\n"))
            except:
                print("\nYou should only put in numbers, please try again:\n ")
            else:
                if rating < 6:

                    break
                else:
                    print("\nYour score is not between 1 to 5\n")


        user_list = [i[1] for i in self.database] #user is sec index
        recipe_list = [i[0] for i in self.database] #recipe is first index
        recipe_user_list = list(zip(recipe_list, user_list)) #can use lists in zip to make a list of tuples as well as dict
        #if the new recipe is in the db override if it is not then replace it
        if (recipe, self.username) in recipe_user_list: #checking if the review has been done for that particular recipe and name
            ind = recipe_user_list.index((recipe, self.username)) #find pos of old review in db
            self.database[ind] = [recipe, self.username, review, rating] #replace old review with the new one in the db
        else:
            self.database.append([recipe, self.username, review, rating]) #if it is not present then just append to the db


        pd.DataFrame(self.database, columns=["Recipe name", "Username", "Review", "Rating"]).to_csv("database.csv") #removed index=false as we want the primary key
        return self.database

    def get_average(self):
        average_df = self.df.groupby(by="Recipe name").agg(["mean", "count"])
        # print(average_df)
        average_df["Rating"] = average_df["Rating"].apply(lambda x: round(x, 2))
        # print(average_df.columns)
        average_df["Average rating"] = average_df["Rating", "mean"]
        average_df["Number of reviews"] = average_df["Rating", "count"]
        average_df["Number of reviews"] = average_df["Number of reviews"].apply(int)
        average_df = average_df.drop(("Rating", "count"), axis=1)
        average_df = average_df.drop(("Rating", "mean"), axis=1)
        return average_df

    #returns the ratings and reviews for a particular recipe
    def explore_db(self):
        self.df = pd.read_csv("database.csv", index_col=0)
        recipe_names = list(set(list(self.df["Recipe name"])))

        for i in range(len(recipe_names)):
            print(f'{i + 1}. {recipe_names[i]}')

        while True:
            try:
                recipe_input = int(input("\nPlease type in the number that corresponds to your recipe choice to see the review and average ratings?\n"))
            except:
                print("\nYou should only put in numbers, please try again:\n ")
            else:
                if recipe_input <= len(recipe_names):
                    break
                else:
                    print("\nYour number is out of range\n")

        recipe = recipe_names[recipe_input - 1]
        temp_db = self.df[self.df["Recipe name"] == recipe]
        for i in range(temp_db.shape[0]):
            print(str(list(temp_db.iloc[i]))[1:-1].replace("'", "")) #iloc lets you query the row with the right index
        avg_rating = temp_db["Rating"].mean()
        print(f'\nThe recipe {recipe} has an average rating of {avg_rating} \n')


    def clear_database(self):
        self.database = self.database[0:0]

        pd.read_csv("database.csv", index_col=0)[0:0].to_csv("database.csv")#not importing index in
