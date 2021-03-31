#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os

type_storage = os.getenv('HBNB_TYPE_STORAGE')


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    @unittest.skipIf(type_storage == 'db', "No apply for db")
    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def test_save_BaseModeldb(self):
        """empty test """
        pass


class test_base_model_v2(unittest.TestCase):
    """ New test class """

    def test001(self):
        """Check if city is child of BaseModel"""
        city = BaseModel()
        self.assertIsInstance(city, BaseModel)

    def test002(self):
        """ Check City default attributes """
        city = BaseModel()
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test004(self):
        """ Check to_dict() function """
        city = BaseModel()
        city_dict = city.to_dict()
        self.assertTrue(type(city_dict) is dict)
        self.assertFalse("_sa_instance_state" in city_dict)

    @unittest.skipIf(type_storage == 'db', "test not possible")
    def test005(self):
        """ Check save() """
        city = BaseModel()
        city.save()
        self.assertNotEqual(city.created_at, city.updated_at)

    @unittest.skipIf(type_storage == 'db', "test not possible")
    def test006(self):
        """ Check delete """
        base = BaseModel()
        base.save()
        base.delete()
        self.assertEqual(1, 1)


@unittest.skipIf(type_storage != "db", "For DB")
class TestBaseModel(unittest.TestCase):
    """ a class for testing the base model """

    @classmethod
    def setUpClass(cls):
        """ Example Data """
        cls.base = BaseModel()
        cls.base.name = "Tabs"
        cls.base.id = "1234"

    @classmethod
    def teardown(cls):
        """ tear down cls """
        del cls.base

    def tearDown(self):
        """ tear down for file storage """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_BaseModel_methods(self):
        """ Check if Basemodel has methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "delete"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_BaseModel_type(self):
        """test if the base is an type BaseModel"""
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_to_dict(self):
        """ test for to_dict """
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertEqual(base_dict['created_at'],
                         self.base.created_at.isoformat())
        self.assertEqual(base_dict['updated_at'],
                         self.base.updated_at.isoformat())
        self.assertRaises(KeyError, lambda: base_dict['_sa_instance_state'])
