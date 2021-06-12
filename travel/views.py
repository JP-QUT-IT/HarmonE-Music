from flask import Blueprint, render_template, request, session, redirect, url_for
from .models import MusicEvent
from . import db

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    events = MusicEvent.query.all()
    return render_template('index.html', events=events)
    if 'email' in session and session['email'] is not None:
        # print(session['email'])
        message = "<h1>Hello " + session['email'] + "</h1>"
    else:
        message = '<h1>HELLO</h1>'
    return message

@mainbp.route('/Forbidden')
def Forbidden():
    return render_template('Error_Handling/Forbidden.html')

@mainbp.route('/events')
def events():
    events = MusicEvent.query.all()
    return render_template('events.html', events=events)

# route to allow users to search
@mainbp.route('/searchtitle')  
def searchtitle():
#get the search string from request  
    if request.args['searchtitle']:
        evntt = "%" + request.args['searchtitle'] + '%'
#use filter and like function to search for matching destinations  
        events = MusicEvent.query.filter(MusicEvent.EventName.like(evntt)).all()  
        #render index.html with few destinations
        return render_template('index.html', events=events)
    else:
        return redirect(url_for('main.index'))

# route to allow users to search
@mainbp.route('/searchgenre')  
def searchgenre():
#get the search string from request  
    if request.args['searchgenre']:
        evntg = "%" + request.args['searchgenre'] + '%'
#use filter and like function to search for matching destinations  
        events = MusicEvent.query.filter(MusicEvent.EventGenre.like(evntg)).all()  
        #render index.html with few destinations
        return render_template('events.html', events=events)
    else:
        return redirect(url_for('main.events'))
