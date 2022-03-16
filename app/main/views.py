from crypt import methods
from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user, login_user, logout_user
from ..models import User, Blogs, Comments
from .forms import CommentForm, BlogsForm, UpdateProfile
from .. import db,photos


@main.route('/')
def index():
    blogs = Blogs.query.all()
    comments = Comments.query.all()
    
    return render_template('index.html', blogs=blogs, comments=comments)




@main.route('/blog/',methods=['GET','POST'])
@login_required
def blogs_form():
    blogs_form = BlogsForm()
    if blogs_form.validate_on_submit():
        title=blogs_form.title.data
        category=blogs_form.category.data
        blog_content=blogs_form.blog_content.data
        
        new_blogs = Blogs(title=title, blog_content=blog_content, category=category,user_id=current_user._get_current_object().id)
        new_blogs.save_pitches()
        return redirect(url_for('.index',))
    
    
    
    return render_template ('blog.html', blogs_form=blogs_form)
        
        

@main.route('/comment/<int:blog_id>', methods = ['GET', 'POST'])
@login_required
def comment(blog_id):
    
    
    comment_form = CommentForm() 
    blogs=Blogs.query.get(blog_id)
    comments= Comments.get_comments(blog_id)
    user = User.query.filter_by(id=id)
    if comment_form.validate_on_submit():
        comments= comment_form.comment.data
        
        new_comment=Comments(blog_id=blog_id, comments=comments, user=user)
        new_comment.save_comments()
        
    return render_template('comment.html', comment_form=comment_form, blogs=blogs,user_id=current_user._get_current_object().id)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
        
    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data
        
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/update.html',form =form)




