try:
    from __init_ import app
    import unittest
    import requests
except Exception as e:
    print("Some modules are missing {}".format(e))

app=app
#check to see if testing file is working
def addTwoNumbers(a,b):
    return a+b


class FlaskTests(unittest.TestCase):

    def test_status(self):
        """Test to check the status code of the api link"""
        #Arrange
        url='https://api.edamam.com/api/recipes/v2?type=public&beta=true&app_id=71b68ced&app_key=e23ca4a79da18cff7d516f5e539033e4'
        #Act
        response=requests.get(url)
        r=response.json()
        #Assert
        assert response.status_code == 200 

    # def test_index_path(self):
    #     response = self.app.get("/")
    #     self.assertEquals(response.status_code, 200)


    # def test_recipe_path(self):
    #     response = self.app.get("/recipes")
    #     self.assertEquals(response.status_code, 200)



if __name__ == "__main__":
    unittest.main()