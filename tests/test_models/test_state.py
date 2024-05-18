import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_instance_creation_with_no_arguments(self):
        """Test if an instance of State is created with no arguments."""
        state = State()
        self.assertIsInstance(state, State)
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertTrue(hasattr(state, 'name'))
        # self.assertEqual(state.name, '')

    def test_instance_creation_with_arguments(self):
        """Test if an instance of State is created with attributes."""
        state_data = {
            'id': '123',
            'created_at': "2022-05-20T10:00:00.000000",
            'updated_at': "2022-05-20T10:00:00.000000",
            'name': 'California'
        }
        state = State(**state_data)
        self.assertEqual(state.id, '123')
        self.assertEqual(state.created_at, datetime(2022, 5, 20, 10, 0, 0))
        self.assertEqual(state.updated_at, datetime(2022, 5, 20, 10, 0, 0))
        self.assertEqual(state.name, 'California')

    def test_update_attributes(self):
        """Test if attributes can be updated."""
        state = State()
        state.name = 'New York'
        self.assertEqual(state.name, 'New York')

    def test_to_dict_method(self):
        """Test if the to_dict() method returns the expected dictionary."""
        state_data = {
            'id': '123',
            'created_at': "2022-05-20T10:00:00.000000",
            'updated_at': "2022-05-20T10:00:00.000000",
            'name': 'California'
        }
        state = State(**state_data)
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['id'], '123')
        self.assertEqual(state_dict['created_at'], '2022-05-20T10:00:00')
        self.assertEqual(state_dict['updated_at'], '2022-05-20T10:00:00')
        self.assertEqual(state_dict['name'], 'California')

    def test_str_representation(self):
        """Test if the __str__() method returns the expected string."""
        state_data = {
            'id': '123',
            'created_at': "2022-05-20T10:00:00.000000",
            'updated_at': "2022-05-20T10:00:00.000000",
            'name': 'California'
        }
        state = State(**state_data)
        str_repr = str(state)
        s0 = "[State] (123) {'id': '123', "
        s1 = "'created_at': datetime.datetime(2022, 5, 20, 10, 0), "
        s2 = "'updated_at': datetime.datetime(2022, 5, 20, 10, 0),"
        s4 = " 'name': 'California'}"
        expected_str = s0 + s1 + s2 + s4
        self.assertEqual(str_repr, expected_str)

    def test_instance_with_additional_attributes(self):
        """Test if an instance of State is created"""
        """with additional attributes."""
        state_data = {
            'id': '123',
            'created_at': "2022-05-20T10:00:00.000000",
            'updated_at': "2022-05-20T10:00:00.000000",
            'name': 'California',
            'population': 10000000,
            'area': 163696
        }
        state = State(**state_data)
        self.assertTrue(hasattr(state, 'population'))
        self.assertTrue(hasattr(state, 'area'))
        self.assertEqual(state.population, 10000000)
        self.assertEqual(state.area, 163696)

    def test_attribute_types(self):
        """Test if attribute types are as expected."""
        state = State()
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)
        self.assertIsInstance(state.name, str)


if __name__ == '__main__':
    unittest.main()
