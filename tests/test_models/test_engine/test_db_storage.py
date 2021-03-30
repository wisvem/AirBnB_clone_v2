#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
from models.base_model import BaseModel
from models import storage
from os import getenv
import models
import MySQLdb

host = "localhost",
port = 3306,
usr = 'hbnb_test',
pwd = 'hbnb_test_pwd',
_db = 'hbnb_test_db',
type_storage = getenv('HBNB_TYPE_STORAGE')


class test_dbstorage(unittest.TestCase):
    """this will test nothing"""

    @unittest.skipIf(type_storage != 'db', "not possible")
    def test_all_returns_dict(self):
        """Check if dictionaty"""
        self.assertIs(type(models.storage.all()), dict)


class TestDBStorage2(unittest.TestCase):
    """a class to test db storage """

    @classmethod
    def setUp(self):
        """Set up MySQL"""
        self.db = MySQLdb.connect(
            host=hst, port=3306, user=usr,  passwd=pwd,  db=_db)
        self.cur = self.db.cursor()
        self.storage = DBStorage()
        self.storage.reload()

    @classmethod
    def tearDown(self):
        """Tear down MySQL"""
        self.cur.close()
        self.db.close()

    @unittest.skipIf(type_storage != 'db', 'Not possible')
    def test_add(self):
        """Test add method"""
        self.cur.execute("""
        INSERT INTO states (id, created_at, updated_at, name)
        VALUES (1, '2017-11-10 00:53:19', '2017-11-10 00:53:19', "California")
        """)
        self.cur.execute('SELECT * FROM states')
        rows = self.cur.fetchall()
        self.assertEqual(len(rows), 1)
