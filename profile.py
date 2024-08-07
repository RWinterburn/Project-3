from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from models import Note
from app import db

profile = Blueprint('profile', __name__)

@profile.route('/profile', methods=['GET', 'POST'])
@login_required
def profile_page():
    if request.method == 'POST':
        note_data = request.form.get('note')
        if note_data:
            new_note = Note(data=note_data, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    notes = Note.query.filter_by(user_id=current_user.id).all()
    return render_template('profile.html', user=current_user, notes=notes)
