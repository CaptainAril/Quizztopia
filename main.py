#!/usr/bin/python3

from models.user import User
from models.question import Question
from models .session import Session

usr_dict_1 = {
    'username': "Johnny",
    'password': 'Johnny123',
    'email': 'Johnny22@email.com'
    }

User_1 = User(**usr_dict_1)
User_1.save()

print(User_1)

# usr_dict_2 = {
#     'username': "Jane",
#     'password': "Jannee",
#     'email': 'Jane02@email.com',
#     'gender': 'female'
# }

# User_2 = User(**usr_dict_2)
# User_2.save()
# print(User_2)

# quest_dict_1 = {
#     'question': 'Who is the president of Nigeria?',
#     'answers': ['Goodluck', 'Obama', 'Buhari', 'Putin', 'Darius'],
#     'correct_answer': 'Buhari'
#     }
# Quest_1 = Question(**quest_dict_1)
# Quest_1.save()
# print(Quest_1)

# import random
# import json

# with open('question.json', 'r') as f:
#     qu_list = json.load(f)

# for item in qu_list:
#     ques = Question(**item)
#     ques.save()

print(User_1.id)

sess_1 = Session(user_id=User_1.id)
sess_1.save()

print(sess_1)