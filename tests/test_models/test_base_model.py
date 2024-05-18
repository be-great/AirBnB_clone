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

    def test_str_(self):
        """Test the string represntation"""
        date = datetime.datetime.today()
        date_rep = repr(date)
        my_model = BaseModel()
        my_model.id = "sdfsdfsd34243"
        my_model.created_at = my_model.updated_at = date
        datestr = my_model.__str__()
        self.assertIn("[BaseModel] (sdfsdfsd34243)", datestr)
        self.assertIn("'id': 'sdfsdfsd34243'", datestr)
        self.assertIn("'created_at': " + date_rep, datestr)
        self.assertIn("'updated_at': " + date_rep, datestr)

    def test_none_args(self):
        """Test none model argmument"""
        my_model = BaseModel(None)
        self.assertNotIn(None, my_model.__dict__.values())

    def test_two_models_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        bm1 = BaseModel()
        time.sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_two_models_different_updated_at(self):
        bm1 = BaseModel()
        time.sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    def test_str_representation(self):
        dt = datetime.datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    def test_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)


if __name__ == '__main__':
    unittest.main()
