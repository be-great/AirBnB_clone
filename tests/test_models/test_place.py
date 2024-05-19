import unittest
from models.place import Place
from datetime import datetime
import json
import models
import time


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
                      'name', 'description', 'number_rooms',
                      'number_bathrooms',
                      'max_guest', 'price_by_night', 'latitude',
                      'longitude',
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
        expected_keys = ['id', 'created_at', 'updated_at',
                         'city_id', 'user_id',
                         'name', 'description', 'number_rooms',
                         'number_bathrooms',
                         'max_guest', 'price_by_night',
                         'latitude', 'longitude',
                         'amenity_ids', '__class__']
        self.assertEqual(place_json['__class__'], 'Place')

    def test_json_deserialization(self):
        """Test the JSON deserialization of Place."""
        place_json = {
            'id': '123',
            'created_at': "2022-05-20T10:00:00.000000",
            'updated_at': "2022-05-20T10:00:00.000000",
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

    def test_to_dicttype(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_idtype(self):
        self.assertEqual(str, type(Place().id))

    def test_city_idtype(self):
        self.assertEqual(str, type(Place.city_id))

    def test_user_idtype(self):
        self.assertEqual(str, type(Place.user_id))

    def test_nametype(self):
        self.assertEqual(str, type(Place.name))

    def test_descriptiontype(self):
        self.assertEqual(str, type(Place.description))

    def test_number_roomstype(self):
        self.assertEqual(int, type(Place.number_rooms))

    def test_number_bathroomstype(self):
        self.assertEqual(int, type(Place.number_bathrooms))

    def test_max_guesttype(self):
        self.assertEqual(int, type(Place.max_guest))

    def test_price_by_nighttype(self):
        self.assertEqual(int, type(Place.price_by_night))

    def test_latitudetype(self):
        self.assertEqual(float, type(Place.latitude))

    def test_longitudetype(self):
        self.assertEqual(float, type(Place.longitude))

    def test_amenity_idstype(self):
        self.assertEqual(list, type(Place.amenity_ids))

    def test_two_model_id(self):
        my_model0 = Place()
        my_model1 = Place()
        self.assertNotEqual(my_model0.id, my_model1.id)

    def test_created_at(self):
        my_model0 = Place()
        time.sleep(1)
        my_model1 = Place()
        self.assertLess(my_model0.created_at, my_model1.created_at)

    """-----------------Filestorage-------------------"""
    """-------------------------------------------------"""


if __name__ == '__main__':
    unittest.main()
