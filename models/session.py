#!/usr/bin/python3

from datetime import datetime
from models.basemodel import Base, BaseModel
from sqlalchemy import Column, ForeignKey, String, Table, DateTime
from sqlalchemy.orm import relationship

session_question = Table('session_question', Base.metadata,
                         Column('question_id', String(60),
                                ForeignKey('questions.id', ondelete='CASCADE', onupdate='CASCADE'),
                                primary_key=True),
                         Column('session_id', String(60),
                                ForeignKey('sessions.id', ondelete='CASCADE', onupdate='CASCADE'),
                                primary_key=True),
                         Column('selected_option', String(60), nullable=True))

class Session(BaseModel, Base):
    __tablename__ = 'sessions'

    created_at = Column(DateTime(), default=datetime.now, nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    questions = relationship('Question', secondary='session_question')
