from flask_wtf import FlaskForm
from wtforms.fields import FileField, TextAreaField, SubmitField, StringField, PasswordField, SelectField, IntegerField
from wtforms.fields.core import DateTimeField
from wtforms.validators import InputRequired, Email, EqualTo
from flask_wtf.file import FileRequired,  FileAllowed

#add the types of files allowed as a set
ALLOWED_FILE = {'png', 'jpg', 'JPG', 'PNG'}

class GenreSearchForm(FlaskForm):
    genre = SelectField('Genres', choices=[('Country', 'COUNTRY'), ('Techno', 'TECHNO'), 
    ('Funk', 'FUNK'), ('Hip Hop', 'HIP HOP'),
    ('Musical', 'MUSICAL'), ('Opera', 'OPERA'),
    ('Jazz', 'JAZZ'), ('Pop', 'POP'),
    ('Punk', 'PUNK'), ('Rock', 'ROCK'),
    ('Blues', 'BLUES'), ('Heavy Metal', 'HEAVY METAL'),
    ('Folk', 'FOLK'), ('Classical', 'CLASSICAL'),
    ('Alternative Rock', 'ALTERNATIVE ROCK'), ('Dance', 'DANCE'),
    ('Disco', 'DISCO'), ('Instrumental', 'INSTRUMENTAL'),
    ('Dubstep', 'DUBSTEP'), ('Orchestra', 'ORCHESTRA')])


class OrderForm(FlaskForm):
  quantity = IntegerField('How Many Tickets Would You Like to Book For This Event?', [InputRequired()])
  submit = SubmitField('Post')


class EventForm(FlaskForm):
  image = FileField('Event Advertisement Image', validators=[FileRequired(message='Image can not be empty'),
          FileAllowed(ALLOWED_FILE, message='Only support png, jpg, JPG, PNG, bmp')])
  name = StringField('Event Title', validators=[InputRequired()])
  genre = SelectField('Genres', choices=[('Country', 'COUNTRY'), ('Techno', 'TECHNO'), 
    ('Funk', 'FUNK'), ('Hip Hop', 'HIP HOP'),
    ('Musical', 'MUSICAL'), ('Opera', 'OPERA'),
    ('Jazz', 'JAZZ'), ('Pop', 'POP'),
    ('Punk', 'PUNK'), ('Rock', 'ROCK'),
    ('Blues', 'BLUES'), ('Heavy Metal', 'HEAVY METAL'),
    ('Folk', 'FOLK'), ('Classical', 'CLASSICAL'),
    ('Alternative Rock', 'ALTERNATIVE ROCK'), ('Dance', 'DANCE'),
    ('Disco', 'DISCO'), ('Instrumental', 'INSTRUMENTAL'),
    ('Dubstep', 'DUBSTEP'), ('Orchestra', 'ORCHESTRA')])
  venue = StringField('Event Venue', validators=[InputRequired()])
  start = StringField('Event Start', validators=[InputRequired()])
  end = StringField('Event End', validators=[InputRequired()])
  tickets = IntegerField('Initial Tickets Available', validators=[InputRequired()])
  status = SelectField('Event Status', choices=[('upcoming', 'UPCOMING'), ('inactive', 'INACTIVE'), ('booked', 'BOOKED'), ('cancelled', 'CANCELLED')])
  description = TextAreaField('Event Description', validators=[InputRequired()])
  submit = SubmitField("Create")


class EditEventForm(FlaskForm):
  image = FileField('Event Advertisement Image', validators=[FileRequired(message='Image can not be empty'),
          FileAllowed(ALLOWED_FILE, message='Only support png, jpg, JPG, PNG, bmp')])
  name = StringField('Event Title', validators=[InputRequired()])
  genre = SelectField('Genres', choices=[('Country', 'COUNTRY'), ('Techno', 'TECHNO'), 
    ('Funk', 'FUNK'), ('Hip Hop', 'HIP HOP'),
    ('Musical', 'MUSICAL'), ('Opera', 'OPERA'),
    ('Jazz', 'JAZZ'), ('Pop', 'POP'),
    ('Punk', 'PUNK'), ('Rock', 'ROCK'),
    ('Blues', 'BLUES'), ('Heavy Metal', 'HEAVY METAL'),
    ('Folk', 'FOLK'), ('Classical', 'CLASSICAL'),
    ('Alternative Rock', 'ALTERNATIVE ROCK'), ('Dance', 'DANCE'),
    ('Disco', 'DISCO'), ('Instrumental', 'INSTRUMENTAL'),
    ('Dubstep', 'DUBSTEP'), ('Orchestra', 'ORCHESTRA')])
  venue = StringField('Event Venue', validators=[InputRequired()])
  start = StringField('Event Start', validators=[InputRequired()])
  end = StringField('Event End', validators=[InputRequired()])
  tickets = IntegerField('Initial Tickets Available', validators=[InputRequired()])
  status = SelectField('Event Status', choices=[('upcoming', 'UPCOMING'), ('inactive', 'INACTIVE'), ('booked', 'BOOKED'), ('cancelled', 'CANCELLED')])
  description = TextAreaField('Event Description', validators=[InputRequired()])
  submit = SubmitField("Edit")
  
  #this should already be there in the forms.py
  
class CommentForm(FlaskForm):
    text = TextAreaField('Comment', [InputRequired()])
    submit = SubmitField('Post')

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[InputRequired("Please enter your username")])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    email = StringField('Email', validators=[Email("Please enter an email address")])
    contact_number = StringField('Contact Number', validators=[InputRequired()])
    address = StringField('Address', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired(),
        EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    usertype = SelectField('Type of User', choices=[('admin', 'ADMIN'), ('customer', 'CUSTOMER')])
    submit = SubmitField('Register As Customer')