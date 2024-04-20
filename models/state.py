#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import os

storage_engine = os.getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    if (storage_engine == 'db'):
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              # cascade="all, delete, delete-orphan"
                              )
    else:
        name = ""

    @property
    def cities(self):
        result = []
        for j, i in models.storage.all(models.city.City).items():
            if (i.state_id == self.id):
                result.append(i)
        return result
        # from models import storage
        # cities = storage.all(City).values()
        # return [city for city in cities if city.state_id == self.id]
