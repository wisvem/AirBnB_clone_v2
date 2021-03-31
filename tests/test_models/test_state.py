#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import unittest
import os
from models.base_model import BaseModel

type_storage = os.getenv('HBNB_TYPE_STORAGE')


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    @unittest.skipIf(type_storage == 'db', "No apply for db")
    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)


class TestState(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.state1 = State()
        cls.state1.name = "CA_the_golden_state"

    @classmethod
    def tearDownClass(cls):
        del cls.state1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.state1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        self.assertIsNotNone(State.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.state1.__dict__)
        self.assertTrue('created_at' in self.state1.__dict__)
        self.assertTrue('updated_at' in self.state1.__dict__)
        self.assertTrue('name' in self.state1.__dict__)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.state1.name), str)

    @unittest.skipIf(type_storage == 'db', "not for db")
    def test_save(self):
        self.state1.save()
        self.assertNotEqual(self.state1.created_at, self.state1.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.state1), True)
