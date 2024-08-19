from flask import Blueprint, render_template, request, flash, redirect, url_for, flash
from flask_login import current_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from models import User, Note, PublicNote
import json

views = Blueprint('views', __name__)



@views.route('/home')
def home():
    return render_template("home.html")


@app.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        public_post = request.form.get('publicpost')

        if public_post:
            # Create a new public note and add it to the database
            new_public_note = PublicNote(content=public_post, user_id=current_user.id)
            db.session.add(new_public_note)
            db.session.commit()
            flash('Public post added successfully!', category='success')
        else:
            flash('Please enter some content for the public post.', category='error')

    # Query the user's private and public notes
    notes = current_user.notes
    public_notes = current_user.public_notes

    return render_template('home.html', user=current_user, notes=notes, public_notes=public_notes)












