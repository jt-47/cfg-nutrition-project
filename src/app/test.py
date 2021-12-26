from run import app
from CALL_API import CallAPI
from Recipe_class import Recipe


from unittest import mock
import unittest
import requests
"""When running the tests use this command: python3 -m unittest discover -s /Users/deeqam/Desktop/cfg_nutrition/cfg-nutrition-project/src/app"""

class FlaskTests(unittest.TestCase):

    app=app
    def test_status(self):
        """Test to check the status code of the api link"""
        #Arrange
        url='https://api.edamam.com/api/recipes/v2?type=public&beta=true&app_id=71b68ced&app_key=e23ca4a79da18cff7d516f5e539033e4'
        #Act
        response=requests.get(url)
        r=response.json()
        #Assert
        assert response.status_code == 200 

    def test_get_nutrients(self):
        """Test to see if nutrients are being returned"""

        recipe = Recipe("Sauteed Chicken Breasts recipes", "https://www.edamam.com/web-img/86b/86bc4ffa518f21fc00764d010015b994", ['4 boneless, skinless chicken breast halves, (6 to 8 ounces each)', 'freshly ground pepper', 'coarse salt', '1 tablespoon olive oil'], 1077.96, {'ENERC_KCAL': {'label': 'Energy', 'quantity': 1077.962845455675, 'unit': 'kcal'}, 'FAT': {'label': 'Fat', 'quantity': 34.3761627986255, 'unit': 'g'}, 'FASAT': {'label': 'Saturated', 'quantity': 6.3668111158246, 'unit': 'g'}, 'FATRN': {'label': 'Trans', 'quantity': 0.05556506532500001, 'unit': 'g'}, 'FAMS': {'label': 'Monounsaturated', 'quantity': 15.336822546250076, 'unit': 'g'}, 'FAPU': {'label': 'Polyunsaturated', 'quantity': 4.810430547626151, 'unit': 'g'}, 'CHOCDF': {'label': 'Carbs', 'quantity': 1.5487794332287503, 'unit': 'g'}, 'CHOCDF.net': {'label': 'Carbohydrates (net)', 'quantity': 0.0, 'unit': 'g'}, 'FIBTG': {'label': 'Fiber', 'quantity': 0.6127305654525002, 'unit': 'g'}, 'SUGAR': {'label': 'Sugars', 'quantity': 0.015499903632000003, 'unit': 'g'}, 'SUGAR.added': {'label': 'Sugars, added', 'quantity': 0.0, 'unit': 'g'}, 'PROCNT': {'label': 'Protein', 'quantity': 178.85362693552577, 'unit': 'g'}, 'CHOLE': {'label': 'Cholesterol', 'quantity': 579.464252675, 'unit': 'mg'}, 'NA': {'label': 'Sodium', 'quantity': 1882.9609398873852, 'unit': 'mg'}, 'CA': {'label': 'Calcium', 'quantity': 51.497494688131276, 'unit': 'mg'}, 'MG': {'label': 'Magnesium', 'quantity': 226.44098858366903, 'unit': 'mg'}, 'K': {'label': 'Potassium', 'quantity': 2683.883695541778, 'unit': 'mg'}, 'FE': {'label': 'Iron', 'quantity': 3.260757634224774, 'unit': 'mg'}, 'ZN': {'label': 'Zinc', 'quantity': 5.430504014515152, 'unit': 'mg'}, 'P': {'label': 'Phosphorus', 'quantity': 1694.5920978841502, 'unit': 'mg'}, 'VITA_RAE': {'label': 'Vitamin A', 'quantity': 56.21896750947501, 'unit': 'µg'}, 'VITC': {'label': 'Vitamin C', 'quantity': 0.0, 'unit': 'mg'}, 'THIA': {'label': 'Thiamin (B1)', 'quantity': 0.7487750573879001, 'unit': 'mg'}, 'RIBF': {'label': 'Riboflavin (B2)', 'quantity': 1.4093617139715, 'unit': 'mg'}, 'NIA': {'label': 'Niacin (B3)', 'quantity': 76.23120001914278, 'unit': 'mg'}, 'VITB6A': {'label': 'Vitamin B6', 'quantity': 6.444657323657676, 'unit': 'mg'}, 'FOLDFE': {'label': 'Folate equivalent (total)', 'quantity': 71.852514465225, 'unit': 'µg'}, 'FOLFD': {'label': 'Folate (food)', 'quantity': 71.852514465225, 'unit': 'µg'}, 'FOLAC': {'label': 'Folic acid', 'quantity': 0.0, 'unit': 'µg'}, 'VITB12': {'label': 'Vitamin B12', 'quantity': 1.66695195975, 'unit': 'µg'}, 'VITD': {'label': 'Vitamin D', 'quantity': 0.0, 'unit': 'µg'}, 'TOCPHA': {'label': 'Vitamin E', 'quantity': 6.407642569402, 'unit': 'mg'}, 'VITK1': {'label': 'Vitamin K', 'quantity': 13.679158020872501, 'unit': 'µg'}, 'Sugar.alcohol': {'label': 'Sugar alcohol', 'quantity': 0.0, 'unit': 'g'}, 'WATER': {'label': 'Water', 'quantity': 586.9179656077343, 'unit': 'g'}}, [])
        nutrients = recipe.get_nutrients()
        exp_nutrients = ['Energy: 1077.96 kcal', 'Fat: 34.38 g', 'Sugars: 0.02 g', 'Protein: 178.85 g', 'Vitamin C: 0.0 mg', 'Potassium: 2683.88 mg', 'Iron: 3.26 mg']
        self.assertEqual(exp_nutrients, nutrients)

    # def test_api_status(self):
    #     """check for a 200 response on index page, from value is always 21"""
    #     """TypeError: __init__() missing 1 required positional argument: 'excluded'"""
    #     api = CallAPI("lemon", "gluten-free", "high-fiber", "sesame")
    #     api.call_api()
    #     self.assertEqual(api.response["from"], 21)  #output returns AssertionError 1!=21

    def test_frontpage(self):
        """Test static frontpage"""
        URL='http://127.0.0.1:5000/'
        r = requests.get(URL)
        self.assertEqual(r.status_code,200)

    def test_recipe_page(self):
        """Test recipe page"""
        URL='http://127.0.0.1:5000/recipes'
        r = requests.get(URL)
        self.assertEqual(r.status_code,200)
    
    def test_about_us_page(self):
        """Test about us page"""
        URL='http://127.0.0.1:5000/aboutus'
        r = requests.get(URL)
        self.assertEqual(r.status_code,200)

    def test_contact_us_page(self):
        """Test contact us page"""
        URL='http://127.0.0.1:5000/contactus'
        r = requests.get(URL)
        self.assertEqual(r.status_code,200)


if __name__ == "__main__":
    unittest.main()