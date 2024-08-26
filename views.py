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
    
    # Check if the current user is the owner of the blog post
    if blog_post.user_id != current_user.id:
        flash('You do not have permission to delete this post.', 'danger')
        return redirect(url_for('views.show_blog_posts'))
    
    db.session.delete(blog_post)
    db.session.commit()
    flash('Blog post deleted successfully!', 'success')
    
    return redirect(url_for('views.show_blog_posts'))
    























