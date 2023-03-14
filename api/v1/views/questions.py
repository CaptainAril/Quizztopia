#!/usr/bin/python3
"""Questions views"""

from api.v1.views import app_views
from models import storage
from models.question import Question
from flask import jsonify, request, abort

@app_views.route('/questions', methods=['GET'])
def get_questions():
    """Retrievs all questions in database."""
    try:
        data = request.get_json()
    except Exception:
        data = None

    filter_questions = []
    count_max = 10
    questions = storage.all(Question).values()
    print(questions)

    if data:
        filter_category = data.get('category')
        filter_difficulty =  data.get('difficulty')
        filter_count = data.get('count')
        filter_type = data.get('type')

        # for question in questions:
        #     if filter_category and question.
    
    quest_list = list(map(lambda x: x.to_dict(), questions))
    return jsonify(quest_list)

@app_views.route('/questions', methods=['POST'])
def create_question():
    """Creates new question object."""
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify(error="Not a Json!"), 400
    not_null = ['question', 'answers', 'correct_answer', 'category_id']
    for key in not_null:
        if key not in data.keys():
            return jsonify(error='{} missing!'.format(key)), 400
    new_question = Question(**data)
    new_question.save()
    return jsonify(new_question.to_dict())


@app_views.route('/questions/<question_id>', methods=['GET', 'PUT', 'DELETE'])
def get_question(question_id):
    """Gets question by its ID and perform operation based on request method."""
    question = storage.get(Question, question_id)

    if question:
        if request.method == 'GET':
            return jsonify(question.to_dict())

        if request.method == 'PUT':
            try:
                data = request.get_json()
            except Exception:
                return jsonify('Not a JSON!'), 400
            ignore = ['id', 'created_at', 'updated_at', '__class__']
            for key, value in data.items():
                if key not in ignore:
                    setattr(question, key, value)
            question.save()
            return jsonify(question.to_dict()), 201

        if request.method == 'DELETE':
            question.delete()
            storage.save()
            return jsonify([])
        
    abort(404)