#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import os

storage_engine = os.getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if (storage_engine == 'db'):
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan"
                              )
    else:
        @property
        def cities(self):
            from models import storage
            cities = storage.all(City)
            cities_states = []
            for key, value in cities_states.items():
                if self.id == value.state_id:
                    cities_states.append(value)
            return cities_states
            # return [city for city in cities if city.state_id == self.id]
