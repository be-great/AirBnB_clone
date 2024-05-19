#!/usr/bin/python3
"""
unittests for models/city.py.
"""

import unittest
from models.city import City
import models
import time


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def testClassDoc(self):
        """Test doc of class"""
        self.assertIsNotNone(City.__doc__)

    def testCityInstance(self):
        """Test if an instance of City is created properly."""
        city = City()
        self.assertIsInstance(city, City)

    def testAttributes(self):
        """Test if City instance has the expected attributes."""
        city = City()
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def testIdNotNone(self):
        """check id != None"""
        self.assertIsNotNone(City().id)

    def testCreateAtNotNone(self):
        """check create_at != None"""
        self.assertIsNotNone(City().created_at)

    def testUpdatedAtNotNone(self):
        """check updated_at != None"""
        self.assertIsNotNone(City().updated_at)

    def testNameNotNone(self):
        """check name != None"""
        self.assertIsNotNone(City().name)

    def testStateIdNotNone(self):
        """check state_id != None"""
        self.assertIsNotNone(City().state_id)

    def testNewAttribute(self):
        """check if new attribute is in __dict__"""
        city = City()
        city.population = 1000000
        status = True if "population" in city.__dict__.keys() else False
        self.assertEqual(True, status)

    def test_to_dicttype(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_idtype(self):
        self.assertEqual(str, type(City().id))

    def test_state_idtype(self):
        self.assertEqual(str, type(City.state_id))

    def test_nametype(self):
        self.assertEqual(str, type(City.name))

    def test_two_model_id(self):
        my_model0 = City()
        my_model1 = City()
        self.assertNotEqual(my_model0.id, my_model1.id)

    def test_created_at(self):
        my_model0 = City()
        time.sleep(1)
        my_model1 = City()
        self.assertLess(my_model0.created_at, my_model1.created_at)

    """-----------------Filestorage-------------------"""
    """-------------------------------------------------"""


if __name__ == '__main__':
    unittest.main()
