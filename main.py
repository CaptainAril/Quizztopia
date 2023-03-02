#!/usr/bin/python3

from models.user import User
from models.question import Question
from models.session import Session
from models import storage
from models.category import Category
import json

categories = [
    'Animals', 
    'Art', 
    'Celebrities', 
    'Entertainment: Board Games', 
    'Entertainment: Books', 
    'Entertainment: Cartoon & Animations', 
    'Entertainment: Comics', 
    'Entertainment: Film', 
    'Entertainment: Japanese Anime & Manga', 
    'Entertainment: Music', 
    'Entertainment: Musicals & Theatres', 
    'Entertainment: Television', 
    'Entertainment: Video Games', 
    'General Knowledge', 
    'Geography', 
    'History', 
    'Mythology', 
    'Politics', 
    'Science & Nature', 
    'Science: Computers', 
    'Science: Gadgets', 
    'Science: Mathematics', 
    'Sports', 
    'Vehicles'
]
# for category in categories:
#     __cat = Category(name=category)
#     __cat.save()


# _ct = {}
# __cats = storage.all(Category)
# for __cat in __cats.values():
#     _ct[__cat.name] = __cat.id


# with open('question.json', 'r') as f:
#     questions = json.load(f)

# for q in questions:
#     if q['category'] in _ct.keys():
#         q['category_id'] = _ct[q['category']]
#         del(q['category'])
#         quest = Question(**q)
#         quest.save()