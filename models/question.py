#!/usr/bin/python3

from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, JSON, Boolean, ForeignKey

class Question(BaseModel, Base):
    """Define question class"""
    __tablename__ = 'questions'

    question = Column(String(1025), nullable=False)
    answers = Column(JSON, nullable=False)
    correct_answer = Column(String(1025), nullable=False)
    type = Column(String(62))
    difficulty = Column(String(62))
    reviewed = Column(Boolean, default=False)
    category_id = Column(String(60), ForeignKey('categories.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    