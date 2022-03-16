from random import choices
from re import sub
from tkinter.tix import InputOnly, Select
from tokenize import String
from turtle import title
from unicodedata import category
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import InputRequired


class SubscriberForm(FlaskForm):
    email = StringField('Add your email address here', validators=[InputRequired()])
    submit =SubmitField('Submit')

class UpdateProfile(FlaskForm):
    
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')
    
class UpdateBog(FlaskForm):
    
    bio = TextAreaField('Add some edits to your blog',validators = [InputRequired()])
    submit = SubmitField('Submit')
    
class BlogsForm(FlaskForm):
    title= StringField('Title:', validators=[InputRequired()])
    blog_content=TextAreaField('Share your blog', validators=[InputRequired()])
    submit= SubmitField('Submit')
    
    
class CommentForm(FlaskForm):
    comment=TextAreaField('Comment', validators=[InputRequired()])
    submit=SubmitField('Submit')
    