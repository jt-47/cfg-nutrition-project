import unittest
from unittest import TestCase
import app
import json
import requests


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
        assert response.status_code ==200 


    def test_api(self):
        """Test to see the if the api dict is the same as printed. Test not working"""
        #Arrange
        url='https://api.edamam.com/api/recipes/v2?type=public&beta=true&app_id=71b68ced&app_key=e23ca4a79da18cff7d516f5e539033e4'
        #Act
        response=requests.get(url)
        r=response.json()
        #Assert 
        assert r['hits'] == 'hits'



if __name__ == "__main__":
    unittest.main()