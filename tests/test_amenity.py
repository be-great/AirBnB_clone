import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_instance_creation_with_no_arguments(self):
        """Test if an instance of Amenity is created with no arguments."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, '')

    def test_instance_creation_with_arguments(self):
        """Test if an instance of Amenity is created with arguments."""
        amenity = Amenity(name="Swimming Pool")
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "Swimming Pool")

    def test_id_type(self):
        """Test if id is of type string."""
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)

    def test_created_at_type(self):
        """Test if created_at is of type datetime."""
        amenity = Amenity()
        self.assertIsInstance(amenity.created_at, datetime)

    def test_updated_at_type(self):
        """Test if updated_at is of type datetime."""
        amenity = Amenity()
        self.assertIsInstance(amenity.updated_at, datetime)

    def test_id_not_none(self):
        """Test if id is not None."""
        amenity = Amenity()
        self.assertIsNotNone(amenity.id)

    def test_created_at_not_none(self):
        """Test if created_at is not None."""
        amenity = Amenity()
        self.assertIsNotNone(amenity.created_at)

    def test_updated_at_not_none(self):
        """Test if updated_at is not None."""
        amenity = Amenity()
        self.assertIsNotNone(amenity.updated_at)

    def test_name_not_none(self):
        """Test if name is not None."""
        amenity = Amenity()
        self.assertIsNotNone(amenity.name)

    def test_name_type(self):
        """Test if name is of type string."""
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)

    def test_name_attribute(self):
        """Test if name attribute is set correctly."""
        amenity = Amenity(name="Gym")
        self.assertEqual(amenity.name, "Gym")

    # Add more test cases as needed...

if __name__ == '__main__':
    unittest.main()
