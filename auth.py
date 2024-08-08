from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from werkzeug.security import check_password_hash, generate_password_hash
from models import User
from app import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:  # Corrected the check for user existence
            if check_password_hash(user.password, password):
                # Login logic
                flash('Log in success', category='success')
                session['user_id'] = user.id
                return redirect(url_for('auth.profile'))  # Redirect to the profile page after login
            else:
                flash('Password is incorrect', category='error')
        else:
            flash('Email does not exist', category='error')

    return render_template('login.html')

@auth.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logged out successfully', category='success')
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category='error')
        elif len(first_name) < 2:
            flash('Name must be greater than 2 characters', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters long', category='error')
        else:
            # Hash the actual user input password
            hashed_password = generate_password_hash(password1, method='pbkdf2:sha256', salt_length=8)
            new_user = User(email=email, first_name=first_name, password=hashed_password)

            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully', category='success')
            return redirect(url_for('auth.login'))  # Redirect to the login page after successful signup
             
    return render_template('sign-up.html')

@auth.route('/profile', methods=['GET', 'POST'])
def profile():
    user_id = session.get('user_id')
    if not user_id:
        flash('You need to log in to view your profile', category='error')
        return redirect(url_for('auth.login'))
    
    user = User.query.get(user_id)
    if not user:
        flash('User not found', category='error')
        return redirect(url_for('auth.login'))

    return render_template('profile.html', user=user)

@auth.route('/')
def home():
    return render_template('home.html')  # Ensure you have a home.html template





