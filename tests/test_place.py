import unittest
from models.place import Place
from datetime import datetime
import json
import pep8


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_instance_creation(self):
        """Test if an instance of Place is created properly."""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_attributes(self):
        """Test if Place instance has the expected attributes."""
        place = Place()
        attributes = ['id', 'created_at', 'updated_at', 'city_id', 'user_id',
                      'name', 'description', 'number_rooms', 'number_bathrooms',
                      'max_guest', 'price_by_night', 'latitude', 'longitude',
                      'amenity_ids']
        for attribute in attributes:
            self.assertTrue(hasattr(place, attribute))

    def test_attribute_types(self):
        """Test if attributes have the correct types."""
        place = Place()
        self.assertIsInstance(place.id, str)
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)

    def test_str_representation(self):
        """Test the __str__ method of Place."""
        place = Place()
        string_representation = str(place)
        self.assertIn("[Place]", string_representation)
        self.assertIn("'id':", string_representation)
        self.assertIn("'created_at':", string_representation)
        self.assertIn("'updated_at':", string_representation)

    def test_to_dict_method(self):
        """Test the to_dict method of Place."""
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        for key in place_dict:
            self.assertTrue(hasattr(place, key))
        self.assertEqual(place_dict['__class__'], 'Place')

    def test_json_representation(self):
        """Test the JSON serialization of Place."""
        place = Place()
        place_json = place.to_dict()
        expected_keys = ['id', 'created_at', 'updated_at', 'city_id', 'user_id',
                         'name', 'description', 'number_rooms', 'number_bathrooms',
                         'max_guest', 'price_by_night', 'latitude', 'longitude',
                         'amenity_ids', '__class__']
        self.assertEqual(sorted(place_json.keys()), sorted(expected_keys))
        self.assertEqual(place_json['__class__'], 'Place')

    def test_json_deserialization(self):
        """Test the JSON deserialization of Place."""
        place_json = {
            'id': '123',
            'created_at': '2022-05-20T10:00:00',
            'updated_at': '2022-05-20T10:00:00',
            'city_id': '456',
            'user_id': '789',
            'name': 'Test Place',
            'description': 'A test place',
            'number_rooms': 2,
            'number_bathrooms': 1,
            'max_guest': 4,
            'price_by_night': 100,
            'latitude': 123.456,
            'longitude': -78.90,
            'amenity_ids': ['123', '456']
        }
        place = Place(**place_json)
        self.assertEqual(place.id, '123')
        self.assertEqual(place.city_id, '456')
        self.assertEqual(place.user_id, '789')
        self.assertEqual(place.name, 'Test Place')
        self.assertEqual(place.description, 'A test place')
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 123.456)
        self.assertEqual(place.longitude, -78.90)
        self.assertEqual(place.amenity_ids, ['123', '456'])

    def test_pep8_city(self):
        """Test PEP8 compliance for City class"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        msg = "fix pep8: " + str(result.messages)
        self.assertEqual(result.total_errors, 0, msg)

if __name__ == '__main__':
    unittest.main()
