from app import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.integer, primary_key=True)
    data = db.Column(db.String(1000))
    user_id = db.column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='notes')