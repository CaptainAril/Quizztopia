#!/usr/bin/python3
"""Flask application"""

from models import storage
from api.v1.views import app_views, auth
from flask import Flask, jsonify, render_template
from flask_login import LoginManager, current_user, login_required
from models.user import User
from models.category import Category

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ssq-3srzy-dsgg-4'

app.register_blueprint(app_views)
app.register_blueprint(auth)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return storage.get(User, user_id)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.username)

@app.route('/play')
def play():
    categories = storage.all(Category)
    return render_template('play.html', categories=categories.values())

@app.route('/stats', methods=['GET'])
def get_stats():
    objs = ['Category', 'Question', 'User']
    obj_dict = {}
    for obj in objs:
        obj_dict[obj] = len(storage.all(obj))
    return jsonify(obj_dict)

@app.teardown_appcontext
def teardown(exception):
    """Tear down method."""
    storage.close()


@app.errorhandler(404)
def error_404(error):
    """Handles the 404 HTTP error."""
    return jsonify(error="Not found"), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000, threaded=True, debug=True)