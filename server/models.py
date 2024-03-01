from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData, event, func, select
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

from sqlalchemy.ext.hybrid import hybrid_property
from config import *

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    feed = db.relationship('Feed', back_populates='user')

    @hybrid_property
    def password(self):
            return self._password_hash
        
    @password.setter
    def password(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self,password):
        return bcrypt.check_password_hash(self._password_hash,password.encode('utf-8'))
    
    # serialize_rules = ('-user._password_hash', '-user.feed', '-feed.user', '-feed.news_item', '-news_item.feed', '-news_item.user', '-user.news_item', '-news_item.category', '-category.news_item', '-category.news_item',)
    
class Feed(db.Model, SerializerMixin):
    __tablename__ = 'feeds'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', back_populates='feed')
    news_item = db.relationship('NewsItem', back_populates='feed')

class Category(db.Model, SerializerMixin):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    news_item = db.relationship('NewsItem', back_populates='category')

class NewsItem(db.Model, SerializerMixin):
     __tablename__ = 'news_items'

     id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String, nullable=False)
     url = db.Column(db.String, nullable=False)
     category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
     feed_id = db.Column(db.Integer, db.ForeignKey('feeds.id'))

     category = db.relationship('Category', back_populates='news_item')
     feed = db.relationship('Feed', back_populates='news_item')



