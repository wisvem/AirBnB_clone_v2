#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

type_storage = getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if type_storage == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete')
    else:
        name = ""

        @property
        def cities(self):
            """Puto el que lo lea"""
            city_dict = models.storage.all(City)
            city_list = []
            for city in city_dict.values():
                if (city.state_id == self.id):
                    city_list.append(city)
            return city_list
