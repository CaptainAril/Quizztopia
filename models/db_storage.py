#!/usr/bin/python3
"""Database Storage Class"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.basemodel import Base
import models
from models.user import User
from models.question import Question
from models.category import Category
from models.session import Session

classes = {
    "User": User,
    "Question": Question,
    "Session": Session,
    "Category": Category
    }

class DBStorage:
    """Interacts with the MySql database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiates a DBStorage object"""

        MYSQL_USER = 'CaptainE'
        MYSQL_PWD = '2475464_Bl'
        MYSQL_DB = 'CaptainE$Quizztopia_dev_db'
        MYSQL_HOST = 'CaptainE.mysql.pythonanywhere-services.com'

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/{}".format(
                                      MYSQL_USER,
                                      MYSQL_PWD,
                                      MYSQL_HOST,
                                      MYSQL_DB
                                    ), pool_pre_ping=True)


    def reload(self):
        # Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def all(self, cls=None):
        obj_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    obj_dict[key] = obj
        return obj_dict

    def get(self, cls, id=None, **kwargs):
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for obj in all_cls.values():
            for key, value in kwargs.items():
                try:
                    if  getattr(obj, key) == value:
                        return obj
                except Exception as e:
                    print(e)
                    return None

            if obj.id == id:
                return obj
        
        return None
    
    def close(self):
        """Calls remove \method on the private session attribute."""
        self.__session.remove()
