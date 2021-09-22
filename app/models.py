#!flask/bin/python
from app import db


class User(db.Model):
    """
    A User model created to save user opinion about a movie
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    movie = db.Column(db.String(800), index=True)
    opinion = db.Column(db.String(15))

    def __repr__(self):
        return '<User {}>'.format(self.username)
