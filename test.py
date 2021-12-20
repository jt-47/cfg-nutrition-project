import unittest
from unittest import TestCase
import app

def addTwoNumbers(a,b):
    return a+b


class FlaskTests(unittest.TestCase):

    def test_add(self):
        c= addTwoNumbers(5,10)
        self.assertEqual(c,15)
        

    def test_index(self):
        tester=app.home(self)
        response=tester.get('/')
        statuscode=response.status_code
        self.assertEqual(statuscode,200)


    # def test_frontpage(self):
    #         """Test static frontpage"""

    #         result = self.client.get("/")

    #         self.assertIn("Enter", result.data)

if __name__ == "__main__":
    unittest.main()