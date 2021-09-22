#!flask/bin/python
from app import app
from flask import render_template, request
import requests
from app import db
from .models import User
import sqlite3 as sql
from config import IMDB_API, IMDB_API_KEY


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
	"""
	Route to display homepage/index page with list to top 250 movies
	"""
	headers = {
		'Accept': 'application/json',
	}
	url = IMDB_API + '/Top250Movies/' + IMDB_API_KEY
	# Get top 250 movies from IMDB API
	r = requests.get(url, headers=headers)
	json_obj = r.json()

	return render_template('index.html', result=json_obj['items'])


@app.route('/movieDetails', methods=['GET'])
def search_movie():
	"""
	Route to fetch the details based on a movie title from IMDB API
	"""
	movie = request.args.get('movie')
	headers = {
		'Accept': 'application/json',
	}
	url = IMDB_API + '/SearchMovie/' + IMDB_API_KEY + '/' + movie
	# Get movie details from IMDB API
	r = requests.get(url, headers=headers)
	json_obj = r.json()

	return render_template('details.html', movie=movie, result=json_obj['results'])


@app.route('/saveOpinion', methods=['POST'])
def save_opinion():
	"""
	Route to save user opinion to SQLite database
	"""
	movie = request.form['movie']
	opinion = request.form['opinion']

	# Connection to the database
	con = sql.connect("app.db")
	cur = con.cursor()

	# Check if opinion on the movie already exists
	cur.execute("SELECT id FROM user WHERE movie=?", (movie,))
	row = cur.fetchone()

	# If yes, update the opinion otherwise
	# insert new one
	if not row:
		# Adding the user opinion to the database
		u = User(username="John", movie=movie, opinion=opinion)
		db.session.add(u)
		db.session.commit()
	else:
		# Update the user opinion
		uid = row[0]
		cur.execute("UPDATE user SET opinion=? WHERE id=?", (opinion, uid))
		con.commit()
	return ''


