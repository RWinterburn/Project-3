from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

# Initialize the database
db = SQLAlchemy()
DB_NAME = "database.db"
admin = Admin()


def create_app():
    app = Flask(__name__, template_folder='app/templates')
    app.config["SECRET_KEY"] = "secret"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    csrf = CSRFProtect(app)
    

    # Initialize the database with the app
    db.init_app(app)
    admin.init_app(app)
    
    # Import models here to avoid circular imports
    from models import User, Note, BlogPost, Comment

    admin.add_view(ModelView(User, db.session))
    # You can add other models similarly if needed
    admin.add_view(ModelView(BlogPost, db.session))
    admin.add_view(ModelView(Comment, db.session))

    # Initialize LoginManager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    from views import views
    from auth import auth


    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    csrf = CSRFProtect(app)

    # Create database if it doesn't exist
    with app.app_context():
        create_database()

    return app

def create_database():
    if not path.exists('app/' + DB_NAME):
        db.create_all()
        print('Created Database')




    
