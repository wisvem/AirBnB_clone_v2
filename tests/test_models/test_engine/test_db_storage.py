#!/usr/bin/python3
""" """
import os
import unittest

type_storage = os.getenv('HBNB_TYPE_STORAGE')


@unittest.skipIf(type_storage != 'db', "apply for db")
class TestDataBase(unittest.TestCase):
    """this will test the console"""

    def test_db(self):
        """ test database """
        pass
