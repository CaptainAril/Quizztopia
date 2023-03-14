from flask import render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from api.v1.views import auth
from models import storage
from models.user import User


@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    if confirm_password != password:
        flash('Passwords must match!')
        return redirect(url_for('auth.signup'))

    user = storage.get(User, email=email, username=username)
    if user:
        if user.username == username:
            flash('Username already exists')

        if user.email == email:
            flash('Email address already exists')
        
        return redirect(url_for('auth.signup'))
    
    new_user = User(username=username, email=email, password=generate_password_hash(password, method='sha256'))
    new_user.save()

    return redirect(url_for('auth.login'))


@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = storage.get(User, username=username)
    print(user)
    # chex = check_password_hash(user.password, password)
    # print(chex)
    # passw = generate_password_hash(password, method='sha256')
    # print(passw)

    

    if not user:
        flash('Username `{}` does not exist!'.format(username))
        return redirect(url_for('auth.login'))
    if not check_password_hash(user.password, password):
        flash('Incorrect password!')
        return redirect(url_for('auth.login'))
    
    login_user(user, remember=remember)
    return redirect(url_for('profile'))
