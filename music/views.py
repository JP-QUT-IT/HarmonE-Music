from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from .models import MusicEvent
from .forms import GenreSearchForm
from . import db

mainbp = Blueprint('main', __name__)

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

@mainbp.route('/Error_404')
def Error_404():
    return render_template('Error_Handling/404.html')

@mainbp.route('/Error_500')
def Error_500():
    return render_template('Error_Handling/500.html')

@mainbp.route('/Error-403')
def Error_403():
    return render_template('Error_Handling/403.html')

@mainbp.route('/events')
def events():
    events = MusicEvent.query.all()
    return render_template('events.html', events=events)

# route to allow users to search
@mainbp.route('/search')  
def search():
#get the search string from request  
    if request.args['search']:
        evnt = "%" + request.args['search'] + '%'
#use filter and like function to search for matching destinations  
        events = MusicEvent.query.filter(MusicEvent.EventName.like(evnt)).all()  
        #render index.html with few destinations
        return render_template('index.html', events=events)
    else:
        return redirect(url_for('main.index'))

@mainbp.route('/genrefilter')  
def genre_filter():
#get the search string from request  
    if request.args['genre_filter']:
        evnt = "%" + request.args['genre_filter'] + '%'
#use filter and like function to search for matching destinations  
        events = MusicEvent.query.filter(MusicEvent.EventGenre.like(evnt)).all()  
        #render index.html with few destinations
        return render_template('index.html', events=events)
    else:
        return redirect(url_for('main.index'))