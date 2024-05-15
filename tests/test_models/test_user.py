#!/usr/bin/python3
"""
unittests for models/city.py.
"""

import models
import unittest
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_user_instance(self):
        """Test if an instance of User is created properly."""
        user = User()
        self.assertIsInstance(user, User)

    def test_user_attributes(self):
        """Test if User instance has the expected attributes."""
        user = User()
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))
