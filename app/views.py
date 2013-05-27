from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html",
		title = 'Home')
@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	return render_template("login.html",
		title = 'Sign In',
		form = form)
@app.route('/register')
def register():
	return render_template("register.html",
		title = 'Register')
@app.route('/user/<username>')
def user_username(username):
	return render_template("user.html",
		title = username,
		username = username)

@app.route('/loggedin/<username>')
def loggedin_user(username):
	return render_template("index.html",
		title = 'Home',
		username = username)

@app.errorhandler(404)
def fourohfour(e):
	return render_template("404.html",
		title = 'Error: 404',)
@app.errorhandler(500)
def fivehundred(e):
	return render_template("500.html",
		title = 'Error: 500')
