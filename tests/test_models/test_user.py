#!/usr/bin/python3
"""
unittests for models/city.py.
"""

import models
import unittest
import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def testClassDoc(self):
        """Test doc of class"""
        self.assertIsNotNone(User.__doc__)

    def testUserInstance(self):
        """Test if an instance of User is created properly."""
        user = User()
        self.assertIsInstance(user, User)

    def testAttributes(self):
        """Test if User instance has the expected attributes."""
        user = User()
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def testIdNotNone(self):
        """check id != None"""
        self.assertIsNotNone(User().id)

    def testCreateAtNotNone(self):
        """check create_at != None"""
        self.assertIsNotNone(User().created_at)

    def testUpdatedAtNotNone(self):
        """check updated_at != None"""
        self.assertIsNotNone(User().updated_at)

    def testFirstNameNotNone(self):
        """check first_name != None"""
        self.assertIsNotNone(User().first_name)

    def testLastNameNotNone(self):
        """check last_name != None"""
        self.assertIsNotNone(User().last_name)

    def testNewAttribute(self):
        """check if new attribute is in __dict__"""
        usr1 = User()
        usr1.name = "Ali"
        status = True if "name" in usr1.__dict__.keys() else False
        self.assertEqual(True, status)

    def test_check_created_updated_is_isoformat(self):
        """check if created_at and updated_at in isoformat"""
        created_at = str(User().created_at)
        updated_at = str(User().updated_at)
        try:

            created_at_obj = datetime.datetime.fromisoformat(created_at)
            updated_at_obj = datetime.datetime.fromisoformat(updated_at)
            self.assertTrue(True)
        except ValueError:
            self.assertTrue(False,
                            f"The created_at or updated_at not in isoformat")

    def test_check_created_at_and_updated_at_notEqual(self):
        """check if created_at != updated_at"""
        created_at = User().created_at
        updated_at = User().updated_at
        self.assertNotEqual(created_at, updated_at)


if __name__ == '__main__':
    unittest.main()
