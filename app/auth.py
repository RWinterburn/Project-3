from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from models import User
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
                #login logic
                flash('Log in success', category = 'success')
                session['user_id'] = user.id
                return redirect(url_for('views.home'))
