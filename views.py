from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from app import db
from models import User, Note, BlogPost, Comment

views = Blueprint('views', __name__)

@views.route('/home', methods=['GET', 'POST'])

def show_blog_posts():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')

        if title and content:
            new_post = BlogPost(title=title, content=content, user_id=current_user.id)
            db.session.add(new_post)
            db.session.commit()
            flash('Blog post added successfully!', 'success')
        else:
            flash('Both title and content are required.', 'danger')

    blog_posts = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
    return render_template('home.html', blog_posts=blog_posts)

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

    return redirect(url_for('views.show_blog_posts'))

@views.route('/all_blog_posts')
def show_all_blog_posts():
    blog_posts = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
    return render_template('all_blog_posts.html', blog_posts=blog_posts)


@views.route('/delete_blog_post/<int:post_id>', methods=['POST'])
@login_required
def delete_blog_post(post_id):
    blog_post = BlogPost.query.get_or_404(post_id)

    # Check if the current user is the owner OR an admin
    if blog_post.user_id != current_user.id and not current_user.is_admin:
        flash('You do not have permission to delete this post.', 'danger')
        return redirect(url_for('views.show_blog_posts'))

    db.session.delete(blog_post)
    db.session.commit()
    flash('Blog post deleted successfully!', 'success')

    return redirect(url_for('views.show_blog_posts'))

@views.route('/delete_comment/<int:comment_id>', methods=['POST'])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)


    # Check if the current user is the owner   

    if comment.user_id != current_user.id and not current_user.is_admin:
        flash('You do not have permission to delete this comment.', 'danger')
        return redirect(url_for('views.show_blog_posts'))

    db.session.delete(comment)
    db.session.commit()
    flash('Comment deleted successfully!', 'success')

    return redirect(url_for('views.show_blog_posts'))


@views.route('/delete_note/<int:note_id>', methods=['POST'])
@login_required
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    
    # Ensure that the current user is authorized to delete this note
    if note.user_id != current_user.id:
        flash('You do not have permission to delete this note.', 'danger')
        return redirect(url_for('auth.profile'))

    try:
        db.session.delete(note)
        db.session.commit()
        flash('Note deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('An error occurred while deleting the note.', 'danger')

    return redirect(url_for('auth.profile'))



























