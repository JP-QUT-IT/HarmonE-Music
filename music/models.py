## Import Necessary Modules ##
from flask import app
from flask_sqlalchemy import SQLAlchemy
from . import db
from datetime import datetime
from flask_login import UserMixin


## Creation of User Table for Database ##
class User(db.Model, UserMixin):
    __tablename__='users' # Table name #
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    contactnumber = db.Column(db.String(10), index=True, nullable=False)
    addres = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(200), index=True, nullable=False)
    # Add the foreign keys #
    events = db.relationship('MusicEvent', backref='users')
    comments = db.relationship('Comment', backref='users')
    orders = db.relationship('Order', backref='users')


## Creation of MusicEvent Table for Database ##
class MusicEvent(db.Model):
    __tablename__ = 'events' # Table name #
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
    # Add the foreign keys #
    comments = db.relationship('Comment', backref='events')
    orders = db.relationship('Order', backref='events')

    def __repr__(self):
        return "<Name: {}>".format(self.name)


## Creation of Comment Table for Database ##
class Comment(db.Model):
    __tablename__ = 'comments' # Table name #
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    # Add the foreign keys #
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

    def __repr__(self):
        return "<Comment: {}>".format(self.text)


## Creation of Order Table for Database ##
class Order(db.Model):
    __tablename__ = 'orders' # Table name #
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    booked_at = db.Column(db.DateTime, default=datetime.now())
    # Add the foreign keys #
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))