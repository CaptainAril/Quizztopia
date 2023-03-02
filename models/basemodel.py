#!/usr/bin/python3
"""Base model for Quizztopi's models."""

from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models

Base = declarative_base()


class BaseModel:
    """Defines the BaseModel class."""
    id = Column(String(60), unique=True, primary_key=True, nullable=False)
    created_at = Column(DateTime(), default=datetime.now, nullable=False)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    

    def __init__(self, *args, **kwargs):
        """Instatiation of basemodel class"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
         
        for key, value in kwargs.items():
            # if key in ['id', 'created_at', 'updated_at']:
            #     pass
            setattr(self, key, value)


    def to_dict(self):
        model_dict = self.__dict__.copy()
        if '_sa_instance_state' in model_dict:
            del(model_dict['_sa_instance_state'])
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict


    def __str__(self):
        return "{} ({}) {}".format(self.__class__.__name__, self.id, self.to_dict())


    def save(self):
        models.storage.new(self)
        models.storage.save()

    
    def delete(self):
        models.storage.delete(self)
