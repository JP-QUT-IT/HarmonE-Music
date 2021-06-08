from flask import Blueprint, render_template, request, session, redirect, url_for
from .models import Destination

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    destinations = Destination.query.all()
    return render_template('index.html', destinations=destinations)
    if 'email' in session and session['email'] is not None:
        # print(session['email'])
        message = "<h1>Hello " + session['email'] + "</h1>"
    else:
        message = '<h1>HELLO</h1>'
    return message

@mainbp.route('/destinations')
def destinations():
    destinations = Destination.query.all()
    return render_template('destinations.html', destinations=destinations)

# route to allow users to search
@mainbp.route('/search')  
def search():
#get the search string from request  
    if request.args['search']:
        dest = "%" + request.args['search'] + '%'
#use filter and like function to search for matching destinations  
        destinations = Destination.query.filter(Destination.name.like(dest)).all()  
        #render index.html with few destinations
        return render_template('index.html', destinations=destinations)
    else:
        return redirect(url_for('main.index'))
