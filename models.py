from app import db
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    # Define the relationships
    notes = db.relationship('Note', back_populates='user')
    comments = db.relationship('Comment', back_populates='user')
    blog_posts = db.relationship('BlogPost', back_populates='user')

class Note(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    is_public = db.Column(db.Boolean, default=False)
    user = db.relationship('User', back_populates='notes')

class BlogPost(db.Model):
    __tablename__ = 'blog_posts'  # Ensure table name matches the foreign key reference
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # Define the relationships
    comments = db.relationship('Comment', back_populates='blog_post')
    user = db.relationship('User', back_populates='blog_posts')

class Comment(db.Model):
    __tablename__ = 'comments'  # Ensure table name matches the foreign key reference
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    blog_post_id = db.Column(db.Integer, db.ForeignKey('blog_posts.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # Define the relationships
    user = db.relationship('User', back_populates='comments')
    blog_post = db.relationship('BlogPost', back_populates='comments')
