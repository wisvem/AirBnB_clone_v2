#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import unittest
import os


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)


class TestUser(unittest.TestCase):
    """ a class for user tests"""

    @classmethod
    def setUpClass(cls):
        """ Example Data """
        cls.user = User()
        cls.user.first_name = "Madame"
        cls.user.last_name = "Tabitha"
        cls.user.email = "gildedlily@gmail.com"
        cls.user.password = "gildedlily123"

    @classmethod
    def teardown(cls):
        """ Tear down the class """
        del cls.user

    def tearDown(self):
        """ Tear down the file (file storage) """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_docs_user(self):
        """ check for docstrings """
        self.assertIsNotNone(User.__doc__)

    def test_attribute_types_User(self):
        """test attribute type for User"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.first_name), str)
