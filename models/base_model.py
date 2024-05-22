#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if self.id is None:
                setattr(self, 'id', str(uuid.uuid4()))
            if self.created_at is None or self.updated_at is None:
                self.created_at = self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        # if not kwargs:
        #     from models import storage
        #     self.id = str(uuid.uuid4())
        #     self.created_at = datetime.now()
        #     self.updated_at = datetime.now()
        #     # storage.new(self)
        # else:
        #     kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
        #                                              '%Y-%m-%dT%H:%M:%S.%f')
        #     kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
        #                                              '%Y-%m-%dT%H:%M:%S.%f')
        #     del kwargs['__class__']
        #     self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def __repr__(self):
        """
        Return a string representation
        """
        return self.__str__()

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Return dictionary implementation
        """

        result = self.__dict__.copy()
        if "_sa_instance_state" in result:
            del result["_sa_instance_state"]
        result["__class__"] = str(type(self).__name__)
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result

    def delete(self):
        """
        Deletes instances from storage
        """
        from models import storage
        storage.delete(self)
