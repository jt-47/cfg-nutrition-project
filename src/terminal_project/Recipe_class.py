class Recipe:
    def __init__(self, recipe_name, image, recipe_ingredients, calories, total_nutrients, allergies):
        self.recipe_name = recipe_name
        self.image = image
        self.recipe_ingredients = recipe_ingredients
        self.calories = calories
        self.total_nutrients = total_nutrients
        self.allergies = allergies

    def __str__(self):
        return f'Recipe name: {self.recipe_name}\nCalories: {self.calories} kcal\nTotal nutrients: {", ".join(self.get_nutrients())}\nTotal ingredients: {", ".join(self.recipe_ingredients)}\nTotal allergies: {", ".join(self.allergies)}' #do i add allergies, get nutrients, -> .replace("\'", "") -> to get rid of "" in getnutrients

    def get_nutrients(self):
        nutritional_values = ['ENERC_KCAL', 'FAT', 'SUGAR', 'PROCNT', 'VITC', 'K', 'FE']
        nv = dict()
        for i in nutritional_values:
            nv[i] = self.total_nutrients[i]

        nv_list = []
        for k, v in nv.items():
            n_string = ""
            nv[k]["label"] += ":"
            nv[k]["quantity"] = round(nv[k]["quantity"], 2)
            for j in v.values():
                n_string += str(j)
                n_string += " "
            n_string = n_string[:-1]
            nv_list.append(n_string)

        return nv_list


    def get_allergies(self):
        '''
            This is for the developer to print out all the allergies in the list but it is not used in the str function above
          '''
        print(self.allergies)
        for i in self.allergies:
            print(i)

    def get_ingredients(self):
        '''
            This is for the developer to print out all the allergies in the list but it is not used in the str function above
          '''
        for i in self.recipe_ingredients:
            print(i)
