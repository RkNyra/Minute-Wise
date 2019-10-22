from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager



class User(UserMixin,db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(70))
    email = db.Column(db.String(70))
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String)
    pitches_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    comments_id = db.Column(db.Integer,db.ForeignKey('comments.id'))
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    
    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)
    
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    def __repr__(self):
        return f'User {self.username}'
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


class Pitch(db.Model):
    __tablename__='pitches'
    id = db.Column(db.Integer,primary_key = True)
    category = db.Column(db.String(200))
    pitch = db.Column(db.String(255))
    comments_id = db.Column(db.Integer,db.ForeignKey('comments.id'))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'
    
    
class Comment(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")
    pitches = db.relationship('Pitch',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'
   