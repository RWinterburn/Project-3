from flask import Flask, render_template
from flask_sqlalchemy import flask_sqlalchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__, template_folder='app/templates')
    app.config["SECRET KEY"] = "secret"

