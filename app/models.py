
from . import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(120), index=True, unique=True)  
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    comments = db.relationship('Comments', backref='author', lazy='dynamic')
    blogs = db.relationship('Blogs',backref = 'blogger',lazy = "dynamic")

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self): 
        return f'USER {self.username}'

class Blogs(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String())
    blog_content = db.Column(db.String())
    date = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship("Comments", backref ='blog', lazy = "dynamic")
    
    def save_blogs(self):
            db.session.add(self)
            db.session.commit()
            
    @classmethod
    def get_blogs(cls):
            blogs = Blogs.query.filter_by().all()
            return blogs
    
    def __repr__(self):
        return f'User{self.username}'


class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column (db.String())
    blog_id = db.Column(db.Integer,db.ForeignKey("blogs.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    # posted = db.Column(db.DateTime,default=datetime.utcnow)
    def save_comments(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_comments(cls,blog_id):
        comments = Comments.query.filter_by(blog_id=blog_id).all()
        return comments
    

class Quote:
    def __init__(self,author,quote):
        self.quote = quote
        self.author = author
        

class Subscribe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255),unique = True,index = True)

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_subscriber(cls, id):
        blogs= Subscribe.query.filter_by(id=id).all()
        return blogs

    def __repr__(self):
        return f'User {self.username}'






