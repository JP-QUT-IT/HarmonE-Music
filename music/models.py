from flask import app
from flask_sqlalchemy import SQLAlchemy
from . import db
from datetime import datetime
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__='users' # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    contactnumber = db.Column(db.String(10), index=True, nullable=False)
    addres = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(200), index=True, nullable=False)
    events = db.relationship('MusicEvent', backref='users')
    comments = db.relationship('Comment', backref='users')


class MusicEvent(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    EventName = db.Column(db.String(100), index=True, nullable=False)
    EventCreator = db.Column(db.Integer, db.ForeignKey('users.id'))
    EventImage = db.Column(db.String(400), index=True, nullable=False)
    EventGenre = db.Column(db.String(100), index=True, nullable=False)
    EventDescription = db.Column(db.String(200), index=True, nullable=False)
    EventVenue = db.Column(db.String(200), index=True, nullable=False)
    EventStart = db.Column(db.String(200), index=True, nullable=False)
    EventEnd = db.Column(db.String(200), index=True, nullable=False)
    EventTickets = db.Column(db.Integer, index=True, nullable=False)
    EventStatus = db.Column(db.String(200), index=True, nullable=False)

    # ... Create the Comments db.relationship
	# relation to call destination.comments and comment.destination
    comments = db.relationship('Comment', backref='events')

    def __repr__(self): #string print method
        return "<Name: {}>".format(self.name)

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    #add the foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

    def __repr__(self):
        return "<Comment: {}>".format(self.text)
