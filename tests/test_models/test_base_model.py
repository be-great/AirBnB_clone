#!/usr/bin/python3
""" Module : unittests for Base_models class."""

import unittest
from models.base_model import BaseModel
import datetime
import time


class TestBase(unittest.TestCase):
    """   Test documents for the base_model.py file    """
    """------------------------------------------------"""
    def test_file_doc(self):
        """Test doc"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_construct_doc(self):
        """Test doc"""
        self.assertIsNotNone(BaseModel.__init__.__doc__)

    def test_str_doc(self):
        """Test doc"""
        self.assertIsNotNone(BaseModel.__str__.__doc__)

    def test_save_doc(self):
        """Test doc"""
        self.assertIsNotNone(BaseModel.save.__doc__)

    def test_to_dict_doc(self):
        """Test doc"""
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    """                Test processes                  """
    """------------------------------------------------"""

    def test_no_args_instantiates(self):
        """check if we base no argument we will have the same instance"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_not_none(self):
        """check id != None"""
        self.assertIsNotNone(BaseModel().id)

    def test_create_at_not_none(self):
        """check create_at != None"""
        self.assertIsNotNone(BaseModel().created_at)

    def test_updated_at_not_none(self):
        """check updated_at != None"""
        self.assertIsNotNone(BaseModel().updated_at)

    def test_new_attribute(self):
        """check if new attribute is in __dict__"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        status = True if "name" in my_model.__dict__.keys() else False
        self.assertEqual(True, status)

    def test_check_created_updated_is_isoformat(self):
        """check if created_at and updated_at in isoformat"""
        created_at = str(BaseModel().created_at)
        updated_at = str(BaseModel().updated_at)
        try:

            created_at_obj = datetime.datetime.fromisoformat(created_at)
            updated_at_obj = datetime.datetime.fromisoformat(updated_at)
            self.assertTrue(True)
        except ValueError:
            self.assertTrue(False,
                            f"The created_at or updated_at not in isoformat")

    def test_check_created_at_and_updated_at_notEqual(self):
        """check if created_at != updated_at"""
        created_at = BaseModel().created_at
        updated_at = BaseModel().updated_at
        self.assertNotEqual(created_at, updated_at)

    def test_check_save(self):
        """check if save method change update_at everytime"""
        model = BaseModel()
        model.save()
        time0 = str(model.updated_at)
        time.sleep(1)
        model.save()
        time1 = str(model.updated_at)
        self.assertNotEqual(time0, time1)


if __name__ == '__main__':
    unittest.main()
