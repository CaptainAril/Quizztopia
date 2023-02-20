#!/usr/bin/python3

from models.basemodel import Base, BaseModel
from sqlalchemy import Column, String, DateTime, Boolean
from datetime import datetime
from sqlalchemy.orm import relationship
from hashlib import md5

class User(BaseModel, Base):
    """Defines User class"""
    __tablename__ = 'users'

    username = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    gender = Column(String(25), nullable=True)
    nationality = Column(String(35), nullable=True)
    joined_at = Column(DateTime(), default=datetime.now, nullable=False)
    last_logged_in = Column(DateTime(), nullable=True)
    sessions = relationship("Session", backref="user")

    
    def __init__(self, *args, **kwargs):
        if 'password' in kwargs.keys():
            kwargs['password'] = self.set_password(kwargs['password'])
        super().__init__(*args, **kwargs)

    def set_password(self, password):
        """Encodes password"""
        return md5(password.encode()).hexdigest()
    