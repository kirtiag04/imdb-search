#!flask/bin/python
import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Database location
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
IMDB_API = 'https://imdb-api.com/API'
# API Key is hard-coded here because it is a POC,
# in production environment, it is better to either
# use secrets or environment variables for these type of config variables
IMDB_API_KEY = 'k_cs3s8be2'
