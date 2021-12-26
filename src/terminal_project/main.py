from Call_API import CallAPI
from Recipe_class import Recipe
import time

def main():
    username = input("\nPlease enter your name: \n")

    # input one ingredient only as it does not work well with multiple ingredients
    query = input("What ingredient would you like to enter? \n")

    print("\nHere is a list of health options: \n")

    health_list = ["alcohol-cocktail", "alcohol-free", "celery-free", "crustacean-free", "dairy-free", "DASH",
                   "egg-free", "fish-free" "fodmap-free", "gluten-free", "immuno-supportive", "keto-friendly",
                   "kidney-friendly", "kosher", "low-fat-abs", "low-potassium", "low-sugar", "lupine-free",
                   "Mediterranean", "mollusk-free", "mustard-free", "no-oil-added", "paleo", "peanut-free",
                   "pescatarian", "pork-free", "red-meat-free", "sesame-free", "shellfish-free", "soy-free",
                   "sugar-conscious", "sulfite-free", "tree-nut-free", "vegan", "vegetarian", "wheat-free"]

    for i in range(len(health_list)):
        print(f'{i + 1}. {health_list[i]}')

    while True:
        try:
            health_input = int(input("\nPlease type in the number that corresponds to your health choice?\n"))
        except:
            print("\nYou should only put in numbers, please try again:\n ")
        else:
            if health_input <= len(health_list):
                break
            else:
                print("\nYour number is out of range\n")

    health = health_list[health_input-1]

    print("\nHere is a list of diet options: \n")
    diet_list = ["balanced", "high-fiber", "high-protein", "low-carb", "low-fat", "low-sodium"]

    for i in range(len(diet_list)):
        print(f'{i+1}. {diet_list[i]}')

    while True:
        try:
            diet_input = int(input("\nPlease type in the number that corresponds to your diet choice?\n"))
        except:
            print("\nYou should only put in numbers, please try again:\n ")
        else:
            if diet_input <= len(diet_list):
                break
            else:
                print("\nYour number is out of range\n")

    diet = diet_list[diet_input-1]

    excluded = input("\nWhat are you allergic to?\n")

    api = CallAPI(username, query, health, diet, excluded)
    # gets the response
    api.call_api()

    # choosing the keys that we want -> returning the api messy data

    api.get_recipe_info()

    # print(api.recipe_info) #api object allows you to access the messy recipe info -> put in the recipe class to filter in the order of the init params
    recipe_dict = dict()
    for i in range(1, 21):
        recipe_dict[f'Recipe {i}'] = Recipe(api.recipe_info[i-1]["recipe_name"], api.recipe_info[i-1]["image"], api.recipe_info[i-1]["recipe_ingredients"], api.recipe_info[i-1]["calories"], api.recipe_info[i-1]["total_nutrients"], api.recipe_info[i-1]["allergies"])

    # printing out everything in the recipe dictionary
    for k, v in recipe_dict.items():
        print(k + ":")
        print(v)
        print("\n")
        time.sleep(1.0)

    # ask the user if they want to review a recipe
    while True:
        recipe_flag = input("\nWould you like to review a recipe? Y or N\n")
        if recipe_flag.upper() == "Y":
            api.ask_user()
        elif recipe_flag.upper() == "N":
            break
        else:
            print("\nYou have not entered the correct parameters, please input Y or N.\n")
        # change to print(api.ask_user()) if you want to see what is in the db as the ask_user function returns self.database

    # ask the user if they want to review another recipe
        while True:
            review_flag = input("\nDo you want to review another recipe? Y or N\n")
            if review_flag.upper() == "Y":
                api.ask_user()
            elif review_flag.upper() == "N":
                break
            else:
                print("\nYou have not entered the correct parameters, please input Y or N.\n")
        break
    # prints the database after seeing it
    # print(api.database)

    # return average rating for the recipe -> get_average()["average rating"]
    # print(api.get_average())

    #uncomment when you want to clear the db -> don't get rid of
    # api.clear_database()
    # print(api.database) #see cleared db

    # print("")

    #use explore database to retrieve the recipe's reviews based on the recipe number
    while True:
        view_ratings = input("\nWould you like to see the review and average ratings for a particular recipe? Y or N\n").upper()
        if view_ratings == "Y":
            api.explore_db()
            while True:
                view_ratings = input("\nWould you like to see the review and average ratings for another recipe? Y or N\n").upper()
                if view_ratings == "Y":
                    api.explore_db()
                elif view_ratings == "N":
                    break
                else:
                    print("\nYou have not entered the correct parameters, please input Y or N.\n")
            break
        elif view_ratings == "N":
            break
        else:
            print("\nYou have not entered the correct parameters, please input Y or N.\n")

if __name__== '__main__':
    #reruns the whole code until a new user does not want to be entered
    while True:
        main()
        if input("\nWould you like to enter another user: Y or N\n").upper() == "N":
            print("\nThank you, see you again next time!\n")
            break



