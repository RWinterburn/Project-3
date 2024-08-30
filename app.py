from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from os import path, environ
from flask_login import LoginManager, current_user
from flask_wtf.csrf import CSRFProtect
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from dotenv import load_dotenv


load_dotenv()


db = SQLAlchemy()
DB_NAME = "database.db"
admin = Admin()

def create_app():
    app = Flask(__name__, template_folder='app/templates')
    

    app.config["SECRET_KEY"] = environ.get("SECRET_KEY", "default_secret_key")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    csrf = CSRFProtect(app)


    db.init_app(app)
    admin.init_app(app)


    from models import User, Note, BlogPost, Comment


    class AdminModelView(ModelView):
        def is_accessible(self):
            return current_user.is_authenticated and current_user.is_admin

        def inaccessible_callback(self, name, **kwargs):

            return redirect(url_for('auth.login'))


    admin.add_view(AdminModelView(User, db.session))
    admin.add_view(AdminModelView(BlogPost, db.session))
    admin.add_view(AdminModelView(Comment, db.session))
    admin.add_view(AdminModelView(Note, db.session))


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    from views import views
    from auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    @app.route('/secret-admin')
    def secret_admin():
        if current_user.is_authenticated and current_user.is_admin:
            return redirect('/admin')
        return redirect(url_for('auth.login'))

    csrf = CSRFProtect(app)


    with app.app_context():
        create_database()

    return app

def create_database():
    if not path.exists('app/' + DB_NAME):
        db.create_all()
        print('Created Database')



    
