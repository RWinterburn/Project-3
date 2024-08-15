from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "database.db"

login_manager = LoginManager()

login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__, template_folder='app/templates')
    app.config["SECRET_KEY"] = "secret"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)


    from views import views
    from auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    with app.app_context():
        from models import User, Note
        create_database()

    return app

def create_database():
    if not path.exists('app/' + DB_NAME):
        db.create_all()
        print('Created Database')



    

