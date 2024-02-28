from flask import Flask, request, make_response, jsonify, session
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS
from models import *
from config import api, app, db, secret_key, bcrypt
import json
from datetime import datetime

#Get all users, Create new users
class Users_Route(Resource):
    def get(self):
        all_users = User.query.all()
        user_dict =[]
        for user in all_users:
            user_dict.append(user.to_dict(rules = ('-user._password_hash', '-user.feed', '-feed.user')))
        return make_response(user_dict, 200)
    def post(self):
        data = request.get_json()
        try:
            data = request.get_json()
            new_user = User(username=data['username'], password=data['password'], email=data['email'])
            db.session.add(new_user)
            db.session.commit()
            return make_response(new_user.to_dict(), 201)
        except:
            return make_response("Invalid request", 400)
        
api.add_resource(Users_Route, '/users')

class Feeds_Route(Resource):
    def get(self):
        all_feeds = Feed.query.all()
        feed_dict =[]
        for feed in all_feeds:
            feed_dict.append(feed.to_dict(rules = ('-feed.user', '-user.feed', '-feed.news_item', '-user._password_hash')))
        return make_response(feed_dict, 200)
    def post(self):
        data = request.get_json()
        try:
            new_feed = Feed(name=data['name'], user_id=data['user_id'])
            db.session.add(new_feed)
            db.session.commit()
            return make_response(new_feed.to_dict(), 201)
        except:
            return make_response("Invalid request", 400)
        
api.add_resource(Feeds_Route, '/feeds')


if __name__ == '__main__':
    app.run(port=5555, debug=True)
