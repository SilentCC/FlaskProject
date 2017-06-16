#!/bin/python

from flask import Flask,make_response,render_template,session,redirect,url_for,flash
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from flask.ext.sqlalchemy import SQLAchemy


app = Flask(__name__)
app.config['SECRET_KEY']='lulu i love you'
app.config['SQLALCHEMY_DATABASE_URI']=\
    'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


db=SQLAchemy(app)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


"""网页表格"""
class NameForm(Form):
    name=StringField('What is your name?',validators=[Required()])
    submit=SubmitField('Submit')


"""数据库"""
class Role(db.Model):
    __tablename__='roles'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),unique=True,index=True)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/hello')
def hello():
    return '<h1>Hello World!</h1>'

from datetime import datetime
@app.route('/index',methods=['GET','POST'])
def index():
    """name = None"""
    form = NameForm()
    if form.validate_on_submit():
        """name = form.name.data
        form.name.data = ''"""
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name']=form.name.data
        form.name.data=''
        return redirect(url_for('index'))
    return render_template('index.html',form=form,name=session.get('name'),current_time=datetime.utcnow())

"""
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello ,%s!</h1>' %name
"""

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

@app.route('/cookie')
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
