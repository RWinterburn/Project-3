from flask import Blueprint, render_template, request, flash
from flask_login import current_user
from app import db
from models import User, Note

views = Blueprint('views', __name__)



@views.route('/home')
def home():
    return render_template("home.html")








