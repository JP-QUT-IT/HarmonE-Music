from datetime import datetime
from flask_login import UserMixin
from . import db

# Customer Table
class Customer(db.Model, UserMixin):
    __tablename__='customer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    email = db.Column(db.String(100), index=True, nullable=False)
	
    password_hash = db.Column(db.String(255), nullable=False)
    authenticated = db.Column(db.Boolean, index=True, default=False, nullable=False)

    def __repr__(self):
        return "<ID: {}, Name: {}, EmailID: {}, pwdhash: {}>".format(self.id, self.name, self.email, self.password_hash)
    
    def is_active(self):
        # All Users would be active
        return True

    comments = db.relationship('Comment', backref='user')


# Administrator Table
class Administrator(db.Model):
    __tablename__='administrator'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    email = db.Column(db.String(100), index=True, nullable=False)

    password_hash = db.Column(db.String(255), nullable=False)
    authenticated = db.Column(db.Boolean, index=True, default=False, nullable=False)


class Destination(db.Model):
    __tablename__='destinations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(400))
    image = db.Column(db.String(400))
    currency = db.Column(db.String(3))
    destinations = db.Column('destinations', db.String, db.ForeignKey('tbldestinations.destinations'))

    # Uppercase fk class, backref = lowercase current class
    comments = db.relationship('Comments', backref='destination')

    def __repr__(self):
        return f'Name: {self.name}\nDescription: {self.description}\nImage url: {self.image}\nCurrency: {self.currency}\n'

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())

    # Foreign Keys
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    administrator_id = db.Column(db.Integer, db.ForeignKey('administrator.id'))
    destination_id = db.Column(db.Integer, db.ForeignKey('destination.id'))

    def __repr__(self):
        return f'User: {self.user},\nText: {self.text}\nCreated at: {self.created_at}\n'