#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table

storage_engine = os.getenv("HBNB_TYPE_STORAGE")

# if storage_engine == "db":
place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        primary_key=True, nullable=False
            ),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        primary_key=True, nullable=False
            ))


class Place(BaseModel, Base):
    """ A place to stay """
    # if (storage_engine == 'db'):
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="place"
                           cascade="all, delete")
    amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            viewonly=False
            )
    if os.getenv('HBNB_TYPE_STORAGE') != 'db':

        @property
        def reviews(self):
            """getter function for reviews attribute"""
            review_list = []
            objs_ = models.storage.all(Review)
            for key, value in objs_.items():
                if value.place_id == self.id:
                    review_list.append(value)
            return review_list

        @property
        def amenities(self):
            """getter function for amenity attribute"""
            amenity_list = []
            objs_ = models.storage.all(Amenity)
            for key, value in objs_.items():
                if value.id in self.amenity_ids:
                    amenity_list.append(value)
            return amenity_list
            return result

        @amenities.setter
        def amenities(self, obj):
            """ setter for amenities class """
            if type(obj).__name__ == "Amenity":
                self.amenity_ids.append(obj.id)
