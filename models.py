from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'  
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note', back_populates='user')

class Note(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  
    user = db.relationship('User', back_populates='notes')


class PublicNote(db.Model):
    __tablename__ = 'public_notes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.String(2000))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  
    user = db.relationship('User', back_populates='public_notes')
    public_notes = db.relationship('PublicNote', back_populates='user')
