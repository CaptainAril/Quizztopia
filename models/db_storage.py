#!/usr/bin/python3
"""Database Storage Class"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.basemodel import Base
import models
from models.user import User
from models.question import Question
from models.session import Session

class DBStorage:
    """Interacts with the MySql database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiates a DBStorage object"""

        MYSQL_USER = getenv('MYSQL_USER')
        MYSQL_PWD = getenv('MYSQL_PWD')
        MYSQL_DB = getenv('MYSQL_DB')

        self.__engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                                      MYSQL_USER,
                                      MYSQL_PWD,
                                      MYSQL_DB
                                    ), pool_pre_ping=True)


    def reload(self):
        Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()
