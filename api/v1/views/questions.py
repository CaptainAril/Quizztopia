#!/usr/bin/python3
"""Questions views"""

from api.v1.views import app_views
from models import storage
from models.category import Category
from flask import jsonify

@app_views.route('/categories', methods=['GET'])
def get_categories():
    categories = storage.all(Category)
    cat_list = list(map(lambda x: x.to_dict(), categories.values()))
    return jsonify(cat_list)

@app_views.route('categoriew')