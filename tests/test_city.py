#!/usr/bin/python3
"""
unittests for models/city.py.
"""

import unittest
from models.city import City


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


if __name__ == '__main__':
    unittest.main()
