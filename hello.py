#!/bin/python

from flask import Flask,make_response,render_template
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)

manager = Manager(app)
bootstrap = Bootstrap(app)

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

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500

if __name__ =='__main__':
    manager.run()
