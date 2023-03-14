#!/usr/bin/python3

from models.basemodel import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Category(BaseModel, Base):
    """Category model"""
    __tablename__ = 'categories'

    name = Column(String(62), nullable=False, primary_key=True)
    questions = relationship('Question', backref="category")
