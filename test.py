import unittest
from unittest import TestCase
import app
import json
import requests



def addTwoNumbers(a,b):
    return a+b


class FlaskTests(unittest.TestCase):

    def test_status(self):
        #Arrange
        url='https://api.edamam.com/api/recipes/v2?type=public&beta=true&app_id=71b68ced&app_key=e23ca4a79da18cff7d516f5e539033e4'
        #Act
        response=requests.get(url)
        r=response.json()
        #Assert
        assert response.status_code ==200 


    def test_api(self):
        #Arrange
        url='https://api.edamam.com/api/recipes/v2?type=public&beta=true&app_id=71b68ced&app_key=e23ca4a79da18cff7d516f5e539033e4'
        #Act
        response=requests.get(url)
        r=response.json()
        #Assert 
        assert r['hits'] == 'hits'



if __name__ == "__main__":
    unittest.main()