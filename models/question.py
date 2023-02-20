from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, JSON, Boolean
import json

class Question(BaseModel, Base):
    """Define question class"""
    __tablename__ = 'questions'

    category = Column(String(32), nullable=False)
    question = Column(String(1025), nullable=False)
    answers = Column(JSON, nullable=False)
    correct_answer = Column(String(1025), nullable=False)
    type = Column(String(62))
    difficulty = Column(String(62))
    reviewed = Column(Boolean, default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
