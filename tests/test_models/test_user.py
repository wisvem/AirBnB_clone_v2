#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import unittest
import os
import pep8
from models.base_model import BaseModel

type_storage = os.getenv('HBNB_TYPE_STORAGE')


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    @unittest.skipIf(type_storage == 'db', "No apply for db")
    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    @unittest.skipIf(type_storage == 'db', "No apply for db")
    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    @unittest.skipIf(type_storage == 'db', "No apply for db")
    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    @unittest.skipIf(type_storage == 'db', "No apply for db")
    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)
