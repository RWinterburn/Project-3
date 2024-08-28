from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, current_user, login_required
from models import User, Note
from app import db
from flask_wtf.csrf import CSRFProtect

auth = Blueprint('auth', __name__)
csrf = CSRFProtect()

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)  # Use login_user to handle session management
            flash('Log in success', category='success')
            return redirect(url_for('views.show_blog_posts'))  # Redirect to the blog posts page
        else:
            flash('Invalid email or password', category='error')

    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()  # Use logout_user to handle session management
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
            hashed_password = generate_password_hash(password1, method='pbkdf2:sha256', salt_length=8)
            new_user = User(email=email, first_name=first_name, password=hashed_password)

            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully', category='success')
            return redirect(url_for('auth.login'))
             
    return render_template('sign-up.html')

@auth.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        note_content = request.form.get('note')
        is_public = 'is_public' in request.form  # Check if the "Make this note public" checkbox was checked

        if not note_content or len(note_content) < 1:
            flash('Note is too short', category='error')
        else:
            new_note = Note(data=note_content, user_id=current_user.id, is_public=is_public)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added successfully', category='success')
            return redirect(url_for('auth.profile'))

    return render_template('profile.html', user=current_user)

@auth.route('/')
def home():
    public_notes = Note.query.filter_by(is_public=True).all()
    print(public_notes)  # Print notes to console
    return render_template('home.html', public_notes=public_notes)








    






