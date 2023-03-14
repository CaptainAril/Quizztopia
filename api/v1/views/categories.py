from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.category import Category

@app_views.route('/categories', methods=['GET', 'POST'])
def get_categories():
    """Returns all categories for GET method, creates new category for POST method."""
    if request.method == 'GET':
        categories = storage.all(Category)
        cat_list = list(map(lambda x : x.to_dict(), categories.values()))
        return jsonify(cat_list)
    
    if request.method == 'POST':
        try:
            data = request.get_json()
        except Exception:
            return jsonify(error='Not a JSON!'), 400
        if 'name' not in data.keys():
            return jsonify(error='`name` missing!'), 400
        new_category = Category(**data)
        new_category.save()
        return jsonify(new_category.to_dict()), 201



@app_views.route('/categories/<category_id>', methods=['GET', 'PUT', 'DELETE'])
def get_category(category_id):
    category = storage.get(Category, category_id)
    if category:
        
        if request.method == 'GET':
            cat = {}
            category_questions = list(map(lambda x: x.to_dict(), category.questions))
            cat['name'] = category.name
            cat['questions'] = category_questions
            cat['count'] = len(category_questions)
            return jsonify(cat)
        
        if request.method == 'PUT':
            try:
                data = request.get_json()
            except Exception:
                return jsonify(error="Not a JSON!"), 400
            ignore = ['id', 'created_at', 'updated_at', '__class__']
            for key, value in data.items():
                if key not in ignore:
                    setattr(category, key, value)
            category.save()
            return jsonify(category.to_dict())

        if request.method == 'DELETE':
            category.delete()
            storage.save()
            return jsonify([])


    abort(404)
