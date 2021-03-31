#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import unittest
from models.base_model import BaseModel
import os
type_storage = os.getenv('HBNB_TYPE_STORAGE')


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    @unittest.skipIf(type_storage == 'db', "No apply for db")
    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)


class TestAmenity(unittest.TestCase):
    """this will test the Amenity class"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.amenity = Amenity()
        cls.amenity.name = "Breakfast"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.amenity

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_attributes_Amenity(self):
        """chekcing if amenity have attibutes"""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_is_subclass_Amenity(self):
        """test if Amenity is subclass of Basemodel"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_attribute_types_Amenity(self):
        """test attribute type for Amenity"""
        self.assertEqual(type(self.amenity.name), str)

    @unittest.skipIf(type_storage == 'db', "test not possible")
    def test_save_Amenity(self):
        """test if the save works"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict_Amenity(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.amenity), True)

class TestAmenity(unittest.TestCase):
    """ a class for testing Amenity"""

    @classmethod
    def setUpClass(cls):
        """ Example Data """
        cls.amen = Amenity()
        cls.amen.name = "Wifi"

    def teardown(cls):
        """ tear down Class """
        del cls.amen

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_Amenity_attribute_types(self):
        """ test Amenity attribute types """
        self.assertEqual(type(self.amen.name), str)

    def test_Amenity_is_subclass(self):
        """ test if Amenity is subclass of BaseModel """
        self.assertTrue(issubclass(self.amen.__class__, BaseModel), True)

    def test_Amenity_save(self):
        """ test save() command """
        self.amen.save()
        self.assertNotEqual(self.amen.created_at, self.amen.updated_at)

    def test_Amenity_sa_instance_state(self):
        """ test is _sa_instance_state has been removed """
        self.assertNotIn('_sa_instance_state', self.amen.to_dict())
