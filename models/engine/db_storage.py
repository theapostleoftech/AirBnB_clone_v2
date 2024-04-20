#!/usr/bin/python3
"""
This is the module for the sqlalchemy database
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            os.getenv("HBNB_MYSQL_USER"),
            os.getenv("HBNB_MYSQL_PWD"),
            os.getenv("HBNB_MYSQL_HOST"),
            os.getenv("HBNB_MYSQL_DB"),
            pool_pre_ping=True
        ))

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Empty description
        """
        objects = {}
        if cls:
            result = self.__session.query(cls).all()
        else:
            result = self.__session.query(State, City).all()
            for row in result:
                if isinstance(row, State):
                    cls = State
                else:
                    cls = City
                key = "{}.{}".format(cls.__Name__, row.id)
                objects[key] = row
        return objects

    def new(self, obj):
        """
        Empty description
        """
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False
                ))
