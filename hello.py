#!/bin/python

from flask import Flask,make_response,render_template
from flask.ext.script import Manager

app = Flask(__name__)

manager = Manager(app)

@app.route('/hello')
def hello():
    return '<h1>Hello World!</h1>'

@app.route('/index')
def index():
    return render_template('index.html')

"""
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello ,%s!</h1>' %name
"""

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

@app.route('/')
def index2():
        response=make_response('<h1>This document carries a cookie!</h1>')
        response.set_cookie('answer','42')
        return response

if __name__ =='__main__':
    manager.run()
