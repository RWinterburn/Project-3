from flask import Blueprint, render_template, request, flash, redirect, url_for, session, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from models import User, Note  # Ensure Note is imported
from app import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Log in success', category='success')
                session['user_id'] = user.id
                return redirect(url_for('auth.profile'))
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
            hashed_password = generate_password_hash(password1, method='pbkdf2:sha256', salt_length=8)
            new_user = User(email=email, first_name=first_name, password=hashed_password)

            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully', category='success')
            return redirect(url_for('auth.login'))
             
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

    if request.method == 'POST':
        note_content = request.form.get('note')
        if not note_content or len(note_content) < 1:
            flash('Note is too short', category='error')
        else:
            new_note = Note(data=note_content, user_id=user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added successfully', category='success')
            return redirect(url_for('auth.profile'))

    return render_template('profile.html', user=user)

@auth.route('/')
def home():
    user_id = session.get('user_id')
    if user_id:
        return redirect(url_for('auth.profile'))
    return render_template('home.html')

@auth.route('/delete-note', methods=['POST'])
def delete_note():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'You need to log in to delete notes'}), 403

    data = request.get_json()
    note_id = data.get('noteId')
    
    if not note_id:
        return jsonify({'error': 'Note ID not provided'}), 400

    note = Note.query.get(note_id)
    
    if not note:
        return jsonify({'error': 'Note not found'}), 404

    if note.user_id != user_id:
        return jsonify({'error': 'Unauthorized'}), 403

    try:
        db.session.delete(note)
        db.session.commit()
        return jsonify({'message': 'Note deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An error occurred while deleting the note'}), 500

@auth.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

    






