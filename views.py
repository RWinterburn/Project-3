from flask import Blueprint, render_template, request, flash
from flask_login import current_user

from app import db
from models import User, Note
import json

views = Blueprint('views', __name__)



@views.route('/home')
def home():
    return render_template("home.html")


@views.route('/delete-note', methods=['POST'])
def delete_note():
    # Parse JSON data from the request
    try:
        data = json.loads(request.data)
    except json.JSONDecodeError:
        return jsonify({'error': 'Invalid JSON'}), 400

    # Extract noteId from the parsed data
    noteId = data.get('noteId')
    
    if not noteId:
        return jsonify({'error': 'noteId not provided'}), 400
    
    # Query the note from the database
    note = Note.query.get(noteId)
    
    if note:
        # Check if the note belongs to the current user
        if note.user_id == current_user.id:
            try:
                db.session.delete(note)
                db.session.commit()
                return jsonify({'message': 'Note deleted successfully'}), 200
            except Exception as e:
                db.session.rollback()
                return jsonify({'error': 'Internal server error'}), 500
        else:
            return jsonify({'error': 'Unauthorized'}), 403
    else:
        return jsonify({'error': 'Note not found'}), 404








