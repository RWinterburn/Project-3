from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_required, current_user, LoginManager
from models import User
from app import db

profile = Blueprint('profile', __name__)




@profile.route('/profile', methods=['GET', 'POST'])
@login_required
def profile_page():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        email = request.form.get('email')
        
        user = User.query.get(current_user.id)
        if user:
            user.first_name = first_name
            user.email = email
            user.notes = notes
            
            db.session.commit()
            flash('Profile updated successfully', category='success')
            return redirect(url_for('profile.profile_page'))
    
    return render_template('profile.html', user=current_user)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Log in success', category='success')
            return redirect(url_for('views.home'))
        else:
            flash('Invalid email or password', category='error')
    
    return render_template('login.html', form=form)

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        email = form.email.data
        first_name = form.first_name.data
        password1 = form.password1.data

        if User.query.filter_by(email=email).first():
            flash('Email already exists', category='error')
        else:
            hashed_password = generate_password_hash(password1, method='pbkdf2:sha256', salt_length=8)
            new_user = User(email=email, first_name=first_name, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully', category='success')
            return redirect(url_for('auth.login'))
    
    return render_template('sign-up.html', form=form)