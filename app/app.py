#!/usr/bin/env python3
# app.route is a decorator that registers index and user functions with an instance of the Flask app
# app.route is a decorator that modifies the the instance of the app thereby directing requets to routes to the the specifed show function

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to my app!</h1>'

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'


if __name__ == '__main__':
    app.run(port=5556)