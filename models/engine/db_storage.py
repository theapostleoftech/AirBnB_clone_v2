#!/usr/bin/python3
"""
This is the module for the sqlalchemy database
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
# from models.state import State
# from models.city import City
# from models.user import User
# from models.place import Place
# from models.review import Review
# from models.amenity import Amenity


class DBStorage:
    """This is the Database storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the database engine"""
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
        Queries the current database session
        """
        objects = {}
        if cls is None:
            classess = ['State', 'City', 'User', 'Place', 'Review', 'Amenity']

            for cla in classess:
                results = self.__session.query(eval(cla))
                for obj in results:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objects[key] = obj

        else:
            results = self.__session.query(cls).all()
            for obj in results:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj

        return objects

    def new(self, obj):
        """
        Adds the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates a table in the database
        Create the current database session
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False
                ))

    def close(self):
        """Close session"""
        self.__session.close()
