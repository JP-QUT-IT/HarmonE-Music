## Import Necessary Modules ##
from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from .models import MusicEvent, Order
from .forms import GenreSearchForm
from flask_login import current_user
from . import db

mainbp = Blueprint('main', __name__)


## Creation of Index Route ##
@mainbp.route('/')
def index():
    events = MusicEvent.query.all()
    search = GenreSearchForm(request.form)

    return render_template('index.html', events=events, form = search)
    if 'email' in session and session['email'] is not None:
        # print(session['email'])
        message = "<h1>Hello " + session['email'] + "</h1>"
    else:
        message = '<h1>HELLO</h1>'
    return message


## Creation of 404 Error Route ##
@mainbp.route('/Error_404')
def Error_404():
    return render_template('Error_Handling/404.html')


## Creation of 500 Error Route ##
@mainbp.route('/Error_500')
def Error_500():
    return render_template('Error_Handling/500.html')


## Creation of 403 Error Route ##
@mainbp.route('/Error-403')
def Error_403():
    return render_template('Error_Handling/403.html')


## Creation of Booking History Route ##
@mainbp.route('/history')
def history():
    events = MusicEvent.query.all()
    orders = Order.query.all()
    return render_template('history.html', orders=orders, events=events)


## Creation of Search By Title Route ##
@mainbp.route('/search')  
def search():
    if request.args['search']:
        evnt = "%" + request.args['search'] + '%' 
        events = MusicEvent.query.filter(MusicEvent.EventName.like(evnt)).all()  
        return render_template('index.html', events=events)
    else:
        return redirect(url_for('main.index'))


## Creation of Search By Genre Route ##
@mainbp.route('/genrefilter')  
def genre_filter():
    if request.args['genre_filter']:
        evnt = "%" + request.args['genre_filter'] + '%' 
        events = MusicEvent.query.filter(MusicEvent.EventGenre.like(evnt)).all()  
        return render_template('index.html', events=events)
    else:
        return redirect(url_for('main.index'))