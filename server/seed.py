from app import app
from models import db, User, Feed, Category, NewsItem
import datetime

with app.app_context():
    # db.create_all()

    print("Deleting users...")
    User.query.delete()

    print("Creating users...")
    user1 = User(username='barrettk',email="barrettkowalsky@gmail.com", password="password")
    db.session.add(user1)
    db.session.commit()

    print("Deleting Feeds...")
    Feed.query.delete()

    print("Creating feeds...")
    feed1 = Feed(name="Barrett Doomsday Feed", user_id=1)
    db.session.add(feed1)
    db.session.commit()

    print("Deleting categories...")
    Category.query.delete()

    print("Creating categories...")
    category1 = Category(name="Avian Influenza")
    db.session.add(category1)
    db.session.commit()

    print("Deleting news items...")
    NewsItem.query.delete()
    
    print("Creating news items...")
    news_item1 = NewsItem(title="Penguins in Antarctica are Dying", url="https://www.nytimes.com/2024/01/30/science/antarctica-bird-flu-penguins.html", category_id=1, feed_id=1)
    db.session.add(news_item1)
    db.session.commit()

