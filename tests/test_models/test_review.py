import unittest
from models.review import Review
from datetime import datetime
import models
import time


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_instance_creation_with_no_arguments(self):
        """Test if an instance of Review is created with no arguments."""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.place_id, '')
        self.assertEqual(review.user_id, '')
        self.assertEqual(review.text, '')

    def test_instance_creation_with_arguments(self):
        """Test if an instance of Review is created with attributes."""
        review_data = {
            'id': '123',
            'created_at': "2022-05-20T10:00:00.000000",
            'updated_at': "2022-05-20T10:00:00.000000",
            'place_id': '456',
            'user_id': '789',
            'text': 'Nice place!'
        }
        review = Review(**review_data)
        self.assertEqual(review.id, '123')
        self.assertEqual(review.created_at, datetime(2022, 5, 20, 10, 0, 0))
        self.assertEqual(review.updated_at, datetime(2022, 5, 20, 10, 0, 0))
        self.assertEqual(review.place_id, '456')
        self.assertEqual(review.user_id, '789')
        self.assertEqual(review.text, 'Nice place!')

    def test_update_attributes(self):
        """Test if attributes can be updated."""
        review = Review()
        review.text = 'Updated text'
        self.assertEqual(review.text, 'Updated text')

    def test_to_dict_method(self):
        """Test if the to_dict() method returns the expected dictionary."""
        review_data = {
            'id': '123',
            'created_at': "2022-05-20T10:00:00.000000",
            'updated_at': "2022-05-20T10:00:00.000000",
            'place_id': '456',
            'user_id': '789',
            'text': 'Nice place!'
        }
        review = Review(**review_data)
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['id'], '123')
        self.assertEqual(review_dict['created_at'], '2022-05-20T10:00:00')
        self.assertEqual(review_dict['updated_at'], '2022-05-20T10:00:00')
        self.assertEqual(review_dict['place_id'], '456')
        self.assertEqual(review_dict['user_id'], '789')
        self.assertEqual(review_dict['text'], 'Nice place!')

    def test_str_representation(self):
        """Test if the __str__() method returns the expected string."""
        review_data = {
            'id': '123',
            'created_at': "2022-05-20T10:00:00.000000",
            'updated_at': "2022-05-20T10:00:00.000000",
            'place_id': '456',
            'user_id': '789',
            'text': 'Nice place!'
        }
        review = Review(**review_data)
        str_repr = str(review)
        s0 = "[Review] (123) {'id': '123', 'created_at':"
        s1 = " datetime.datetime(2022, 5, 20, 10, 0)"
        s2 = ", 'updated_at': datetime.datetime(2022, 5, 20, 10, 0),"
        s3 = " 'place_id': '456', 'user_id': '789', 'text': 'Nice place!'}"
        expected_str = s0 + s1 + s2 + s3
        self.assertEqual(str_repr, expected_str)

    def test_instance_with_additional_attributes(self):
        """Test if an instance of Review is created"""
        """with additional attributes."""
        review_data = {
            'id': '123',
            'created_at': "2022-05-20T10:00:00.000000",
            'updated_at': "2022-05-20T10:00:00.000000",
            'place_id': '456',
            'user_id': '789',
            'text': 'Nice place!',
            'rating': 5
        }
        review = Review(**review_data)
        self.assertTrue(hasattr(review, 'rating'))
        self.assertEqual(review.rating, 5)

    def test_attribute_types(self):
        """Test if attribute types are as expected."""
        review = Review()
        self.assertIsInstance(review.id, str)
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)

    def test_class_doc_string(self):
        """Test if the class doc string exists."""
        self.assertTrue(len(Review.__doc__) > 0)

    def test_class_public_attributes(self):
        """Test if class public attributes exist."""
        self.assertTrue(hasattr(Review, 'place_id'))
        self.assertTrue(hasattr(Review, 'user_id'))
        self.assertTrue(hasattr(Review, 'text'))

    def test_class_attributes_type(self):
        """Test if class attributes are of correct type."""
        self.assertIsInstance(Review.place_id, str)
        self.assertIsInstance(Review.user_id, str)
        self.assertIsInstance(Review.text, str)

    def test_class_attributes_default_value(self):
        """Test if class attributes have default values."""
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")

    def test_instance_attributes_default_value(self):
        """Test if instance attributes have default values."""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_instance_attributes_with_arguments(self):
        """Test if instance attributes are set properly."""
        review = Review(place_id="123", user_id="456", text="Test text")
        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.text, "Test text")

    def test_to_dicttype(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_idtype(self):
        self.assertEqual(str, type(Review().id))

    def test_place_idtype(self):
        self.assertEqual(str, type(Review.place_id))

    def test_user_idtype(self):
        self.assertEqual(str, type(Review.user_id))

    def test_texttype(self):
        self.assertEqual(str, type(Review.text))

    def test_two_model_id(self):
        my_model0 = Review()
        my_model1 = Review()
        self.assertNotEqual(my_model0.id, my_model1.id)

    def test_created_at(self):
        my_model0 = Review()
        time.sleep(1)
        my_model1 = Review()
        self.assertLess(my_model0.created_at, my_model1.created_at)


if __name__ == '__main__':
    unittest.main()
