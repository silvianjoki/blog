from ast import Sub
from crypt import methods
from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user, login_user, logout_user
from ..models import User, Blogs, Comments
from .forms import CommentForm, BlogsForm, SubscriberForm, UpdateProfile
from .. import db,photos


@main.route('/')
def index():
    blogs = Blogs.query.all()
    comments = Comments.query.all()
    
    return render_template('index.html', blogs=blogs, comments=comments)


@main.route('/')
def index():
    
    quote= get_random_quote()
    subscriber_form = SubscriberForm()
    if subscriber_form.validate_on_submit():
        subscribe = subscriber_form.email.data
        
        mail_message ('Thanks and welcome to blogga,''email/subscribe', subscribe.email, user=subscribe)
        

        
        return redirect(url_for('.index'))
    
    return render_template('index.html', subscriber_form=subscriber_form, quote=quote)
        

@main.route('/blog/',methods=['GET','POST'])
@login_required
def blogs_form():
    blogs_form = BlogsForm()
    if blogs_form.validate_on_submit():
        title=blogs_form.title.data
        blog_content=blogs_form.blog_content.data
        
        new_blogs = Blogs(title=title, blog_content=blog_content, user_id=current_user._get_current_object().id)
        new_blogs.save_pitches()
        return redirect(url_for('.index',))
    
    
    
    return render_template ('blog.html', blogs_form=blogs_form)
        
        

@main.route('/comment/', methods = ['GET', 'POST'])
@login_required
def comment():
    
    
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comments= comment_form.comment.data
        
        comment=Comments(comments=comments)
        comment.save_comments()
        
    return render_template('comment.html', comment_form=comment_form,user_id=current_user._get_current_object().id)



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




