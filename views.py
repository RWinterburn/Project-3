from flask import Blueprint, render_template, request, flash
from flask_login import current_user
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from models import User, Note, BlogPost, Comment
import json

views = Blueprint('views', __name__)



@views.route('/home')
def home():
    public_notes = Note.query.filter_by(is_public=True).all()
    print(public_notes)  # Print notes to console
    return render_template('home.html', public_notes=public_notes)


#testing
@views.route('/add_comment/<int:post_id>', methods=['POST'])
@login_required
def add_comment(post_id):
    blog_post = BlogPost.query.get_or_404(post_id)
    comment_content = request.form.get('comment')
    
    if comment_content:
        new_comment = Comment(content=comment_content, user_id=current_user.id, blog_post_id=post_id)
        db.session.add(new_comment)
        db.session.commit()
        flash('Comment added successfully!', 'success')
    else:
        flash('Comment cannot be empty.', 'danger')

    return redirect(url_for('home'))

#testing
@views.route('/')
def home():
    blog_posts = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
    return render_template('home.html', blog_posts=blog_posts)























