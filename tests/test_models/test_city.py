#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.base_model import BaseModel
import unittest
import os

type_storage = os.getenv('HBNB_TYPE_STORAGE')


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    @unittest.skipIf(type_storage == 'db', "No apply for db")
    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    @unittest.skipIf(type_storage == 'db', "No apply for db")
    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)


class TestCity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.city1 = City()
        cls.city1.name = "San Francisco"
        cls.city1.state_id = "CA"

    @classmethod
    def tearDownClass(cls):
        del cls.city1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.city1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        self.assertIsNotNone(City.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.city1.__dict__)
        self.assertTrue('created_at' in self.city1.__dict__)
        self.assertTrue('updated_at' in self.city1.__dict__)
        self.assertTrue('state_id' in self.city1.__dict__)
        self.assertTrue('name' in self.city1.__dict__)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.city1.name), str)
        self.assertEqual(type(self.city1.state_id), str)

    @unittest.skipIf(type_storage == 'db', "not for db")
    def test_save(self):
        self.city1.save()
        self.assertNotEqual(self.city1.created_at, self.city1.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.city1), True)
