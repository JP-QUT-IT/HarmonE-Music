from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, SelectField, IntegerField
from wtforms.fields.core import DateTimeField
from wtforms.validators import InputRequired, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

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

class EventForm(FlaskForm):
  name = StringField('Event Title', validators=[InputRequired()])
  image = FileField('Event Advertisement Image', validators=[FileRequired(message='Image can not be empty'),
          FileAllowed(ALLOWED_FILE, message='Only support png, jpg, JPG, PNG, bmp')])
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
  description = TextAreaField('Event Description', validators=[InputRequired()])
  venue = StringField('Event Venue', validators=[InputRequired()])
  start = DateTimeField('Event Start', format='%d/%m/%y', validators=[InputRequired()])
  end = DateTimeField('Event End', format='%d/%m/%y', validators=[InputRequired()])
  tickets = IntegerField('Initial Tickets Available', validators=[InputRequired()])
  status = SelectField('Event Status', choices=[('upcoming', 'UPCOMING'), ('inactive', 'INACTIVE'), ('booked', 'BOOKED'), ('cancelled', 'CANCELLED')])
  submit = SubmitField("Create")


class EditEventForm(FlaskForm):
  name = StringField('Event Title', validators=[InputRequired()])
  image = FileField('Event Advertisement Image', validators=[FileRequired(message='Image can not be empty'),
          FileAllowed(ALLOWED_FILE, message='Only support png, jpg, JPG, PNG, bmp')])
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
  description = TextAreaField('Event Description', validators=[InputRequired()])
  venue = StringField('Event Venue', validators=[InputRequired()])
  start = DateTimeField('Event Start', format='%d/%m/%y', validators=[InputRequired()])
  end = DateTimeField('Event End', format='%d/%m/%y', validators=[InputRequired()])
  tickets = IntegerField('Initial Tickets Available', validators=[InputRequired()])
  status = SelectField('Event Status', choices=[('upcoming', 'UPCOMING'), ('inactive', 'INACTIVE'), ('booked', 'BOOKED'), ('cancelled', 'CANCELLED')])
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