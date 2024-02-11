#!/bin/usr/python3
"""basemodel class"""
from datetime import datetime
from models import storage
import uuid


class BaseModel():
    """Class base model"""

    def __init__(self, *args, **kwargs):
        """initialize basemodel class object"""
        if kwargs:
            for a, b in kwargs.items():
                if a in ('created_at', 'updated_at'):
                    b = datetime.strptime(b, '%Y-%m-%dT%H:%M:%S.%f')
                if a != '__class__':
                    setattr(self, a, b)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """return str representation of object"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """update updated_at"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """return dictionary representation of object"""
        d = dict(self.__dict__)
        d['__class__'] = self.__class__.__name__
        d['created_at'] = datetime.isoformat(self.created_at)
        d['updated_at'] = datetime.isoformat(self.updated_at)
        return d
