from flask import Blueprint, render_template, request, flash
from flask_login import current_user
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from models import User, Note
import json

views = Blueprint('views', __name__)



@views.route('/home')
def home():
    public_notes = Note.query.filter_by(is_public=True).all()
    print(public_notes)  # Print notes to console
    return render_template('home.html', public_notes=public_notes)























