from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, DateField
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
    content=TextAreaField('Share your blog', validators=[InputRequired()])
    date=DateField('Posted', validators=[InputRequired()])
    submit= SubmitField('Submit')
    
    
class CommentForm(FlaskForm):
    comment=TextAreaField('Comment', validators=[InputRequired()])
    submit=SubmitField('Submit')
    