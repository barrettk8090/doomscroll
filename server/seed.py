from app import app
from models import db, User, Feed, Category, NewsItem
import datetime

with app.app_context():
    db.create_all()
    user = User(username='test',