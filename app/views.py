from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html",
		title = 'Home')
@app.route('/login')
def index():
	return render_template("index.html",
		title = 'Home')
@app.route('/register')
def index():
	return render_template("index.html",
		title = 'Home')
@app.route('/user/{{username}}')
def index():
	return render_template("index.html",
		title = 'Home')

@app.errorhandler(404)
def fourohfour(e):
	return render_template("404.html",
		title = 'Error: 404',)
@app.errorhandler(500)
def fivehundred(e):
	return render_template("500.html",
		title = 'Error: 500')
