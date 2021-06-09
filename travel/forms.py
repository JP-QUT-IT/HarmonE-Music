from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, SelectField, IntegerField, DateField
from wtforms.validators import InputRequired, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

#add the types of files allowed as a set
ALLOWED_FILE = {'png', 'jpg', 'JPG', 'PNG'}

class EventForm(FlaskForm):
  name = StringField('Event Title', validators=[InputRequired()])
  image = FileField('Event Advertisement Image', validators=[FileRequired(message='Image can not be empty'),
          FileAllowed(ALLOWED_FILE, message='Only support png, jpg, JPG, PNG, bmp')])
  genre = StringField('Event Genre', validators=[InputRequired()])
  description = TextAreaField('Event Description', validators=[InputRequired()])
  venue = StringField('Event Venue', validators=[InputRequired()])
  start = StringField('Event Start', validators=[InputRequired()])
  end = StringField('Event End', validators=[InputRequired()])
  tickets = IntegerField('Initial Tickets Available', validators=[InputRequired()])
  status = SelectField('Event Status', choices=[('upcoming', 'UPCOMING'), ('inactive', 'INACTIVE'), ('booked', 'BOOKED'), ('cancelled', 'CANCELLED')])
  submit = SubmitField("Create")


class EditEventForm(FlaskForm):
  name = StringField('Event Title', validators=[InputRequired()])
  image = FileField('Event Advertisement Image', validators=[FileRequired(message='Image can not be empty'),
          FileAllowed(ALLOWED_FILE, message='Only support png, jpg, JPG, PNG, bmp')])
  genre = StringField('Event Genre', validators=[InputRequired()])
  description = TextAreaField('Event Description', validators=[InputRequired()])
  venue = StringField('Event Venue', validators=[InputRequired()])
  start = StringField('Event Start', validators=[InputRequired()])
  end = StringField('Event End', validators=[InputRequired()])
  tickets = IntegerField('Initial Tickets Available', validators=[InputRequired()])
  status = SelectField('Event Status', choices=[('upcoming', 'UPCOMING'), ('inactive', 'INACTIVE'), ('booked', 'BOOKED'), ('cancelled', 'CANCELLED')])
  submit = SubmitField("Edit")
  
  #this should already be there in the forms.py
  
class CommentForm(FlaskForm):
    text = TextAreaField('Comment', [InputRequired()])
    submit = SubmitField('Post')

class LoginForm(FlaskForm):
    companyname = StringField('Username',validators=[InputRequired("Please enter your username")])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class CustomerRegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    email = StringField('Email', validators=[Email("Please enter an email address")])
    password = PasswordField('Password', validators=[InputRequired(),
        EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    submit = SubmitField('Register As Customer')

class AdminRegisterForm(FlaskForm):
    companyname = StringField('Company Name', validators=[InputRequired()])
    email = StringField('Email', validators=[Email("Please enter an email address")])
    password = PasswordField('Password', validators=[InputRequired(),
        EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    submit = SubmitField('Register As Administrator')