
from flask import render_template, request, redirect, url_for,abort
from . import main
from .forms import UpdateProfile 
from .forms import CommentsForm, UpdateProfile, BlogForm
from ..request import get_quotes
from ..models import User,Blog,Comment
from flask_login import login_required,current_user
from .. import db,photos
import markdown2 


# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The Blogging'

    blog= Blog.query.all()
    quotes= get_quotes()  

    return render_template('index.html', title = title,quotes=quotes, blog= blog)
   

@main.route('/blog/new/', methods = ['GET','POST'])
@login_required
def new_blog():
    '''
    Function that creates new blogs
    '''
    form = BlogForm()
    if form.validate_on_submit():
        blog = form.content.data
        new_blog= Blog(blog = blog)

        new_blog.save_blog()
        return redirect(url_for('main.index'))

    return render_template('new_blog.html', new_blog_form= form)

@main.route('/blog/<int:id>/update',methods = ['GET','POST'])
@login_required
def update_blog(id):
    blog=Blog.query.filter_by(id=id).first()
    if blog is None:
        abort(404)
    form=BlogForm()
    if form.validate_on_submit():
        blog.title=form.title.data
        blog.content=form.content.data
        # blog.author=form.author.data
        db.session.commit()
        flash('your post has been updated')
        return redirect(url_for('.index'))
    

    return render_template('blog.html', form=form)

# @main.route('/blog/comments/new/<int:id>',methods = ['GET','POST'])
# @login_required
# def new_comment(id):
#     form = CommentsForm()
#     if form.validate_on_submit():
#         comment=form.comment.data
#         new_comment = Comment(user=current_user, comment = comment)
#         new_comment.save_comment()
#         return redirect(url_for('main.index'))
#     comments = Comment.get_comments(id)
#     print(comments)
#     comm=Comment.query.filter_by(id = id)
    
#     return render_template('new_comment.html',comment_form=form,comm = comm)

# @main.route('/view/comment/<int:id>')
# def view_comments(id):
#     '''
#     Function that returs  the comments belonging to a particular quote
#     '''
#     comments = Comment.get_comments(id)
#     print(comments)
#     return render_template('view_comments.html',comments = comments, id=id)

# @main.route('/user/<uname>/update/pic',methods= ['POST'])
# @login_required
# def update_pic(uname):
#     user = User.query.filter_by(username = uname).first()
#     if 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         user.profile_pic_path = path 
#         db.session.commit()
#     return redirect(url_for('main.profile',uname=uname))

# @main.route('/user/<uname>')
# def profile(uname):
#     user = User.query.filter_by(username = uname).first()

#     if user is None:
#         abort(404)

#     return render_template("profile/profile.html", user = user)

# @main.route('/user/<uname>/update',methods = ['GET','POST'])
# @login_required
# def update_profile(uname):
#     user = User.query.filter_by(username = uname).first()
#     if user is None:
#         abort(404)

#     form = UpdateProfile()

#     if form.validate_on_submit():
#         user.bio = form.bio.data

#         db.session.add(user)
#         db.session.commit()

#         return redirect(url_for('.profile',uname=user.username))
    
#     return render_template('profile/update.html',form =form)

# @main.route('/index/<int:id>/delete', methods = ['GET','POST'])
# @login_required
# def delete(id):
#    current_post = Blog.query.filter_by(id = id).first()
#    if current_post.user != current_user:
#        abort(404)
#    db.session.delete(current_post)
#    db.session.commit()
#    return redirect(url_for('main.index'))
   
# @main.route('/index/<int:id>/delete_comment', methods = ['GET','POST'])
# @login_required
# def delete_comment(id):
#    current_post = Comment.query.filter_by(id = id).first()
#    if current_post.user != current_user:
#        abort(404)
#    db.session.delete(current_post)
#    db.session.commit()
#    return redirect(url_for('.index'))
#    return render_template('comments.html',current_post = current_post)

# @main.route('/test/<int:id>')  
# def test(id):
#     '''
#     this is route for basic testing
#     '''
#     blog =blog.query.filter_by(id=1).first()

#     return render_template('test.html',Blog = Blog)