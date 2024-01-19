from .database import db
from flask_login import UserMixin

# Userモデルの定義
class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_name = db.Column(db.String(64), nullable=False)
    mail_address = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    profile_image = db.Column(db.String(255))
    posts = db.relationship('Postinformation', backref='author')
    comments = db.relationship('Comment', backref='commenter')
    goods = db.relationship('Good', backref='owner')

    def to_dict(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'mail_address': self.mail_address,
            'password': self.password,
            'profile_image': self.profile_image
        }
