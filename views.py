from flask import Blueprint, render_template, request, flash
from flask_login import current_user
from app import db
from models import Note

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()  # Call commit as a method
            flash('Note has been added', category='success')
    return render_template("base.html")

@views.route('/home')
def home():
    return render_template("home.html")

