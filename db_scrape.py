#!/usr/bin/python3

import requests
import json

def parse():
    url = 'https://opentdb.com/api.php'
    params = {'amount': 100}

    r = requests.get(url, params=params)

    print(r.status_code, '\n')
    data = r.json()

    quest_list = []
    count = 0

    for question in data['results']:
        try:
            question['answers'] = question['incorrect_answers']
            question['answers'].append(question['correct_answer'])
            del(question['incorrect_answers'])
            quest_list.append(question)
            count += 1
        except Exception as e:
            print(e)
    r.close()
    return quest_list

count = 0
Quizztopia = []

for i in range(10):
    quest_list = parse()
    count += len(quest_list)
    Quizztopia.extend(quest_list)


print("{} questions parsed successfully".format(count))
print(len(Quizztopia))

with open('question.json', 'w') as f:
    json.dump(Quizztopia, f, indent=4)