import re
from flask import ( 
    Blueprint, app, flash, render_template, request, url_for, redirect
) 
from .models import MusicEvent, Comment, Order
from .forms import CommentForm, EventForm, EditEventForm, OrderForm
from flask_login import login_required, current_user
from . import db
import music

#create a blueprint
bp = Blueprint('event', __name__, url_prefix='/events')

#create a page that will show the details fo the destination
@bp.route('/<id>') 
def show(id): 
  event = MusicEvent.query.filter_by(id=id).first()  
  cform = CommentForm()
  return render_template('events/show.html', event=event, form=cform)


@bp.route('/create', methods=['GET','POST'])
@login_required
def create():

  if (current_user.role == 'admin'):
    pass
  elif (current_user.role == 'customer'):
    return redirect('/Forbidden')
  else:
    return redirect('/Forbidden')
  
  print('Method type: ', request.method)
  form = EventForm()
  if(form.validate_on_submit()):
    db_file_path=check_upload_file(form)
    event=MusicEvent(
    EventName=form.name.data, 
    EventCreator=current_user.name,
    EventImage=db_file_path, 
    EventGenre=form.genre.data,
    EventDescription=form.description.data, 
    EventVenue=form.venue.data, 
    EventStart=form.start.data, 
    EventEnd=form.end.data, 
    EventTickets=form.tickets.data, 
    EventStatus=form.status.data)
    db.session.add(event)
    db.session.commit()
    flash('Created event')
    return redirect('/')
  return render_template('events/create.html', form=form)

# @bp.route('/book/<id>', methods=['GET', 'POST'])
# @login_required
# def book(id):
#   selectedEvent = MusicEvent.query.filter_by(id = id).first()

#   return render_template('events/book.html', form=form)


@bp.route('/edit/<id>', methods=['GET', 'POST'])
@login_required
def edit(id):
  selectedEvent = MusicEvent.query.filter_by(id = id).first()

  if (current_user.name==selectedEvent.EventCreator):
    pass
  elif (current_user.role == 'customer'):
    return redirect('/Forbidden')
  else:
    return redirect('/Forbidden')

  form = EditEventForm(name=selectedEvent)
  if form.validate_on_submit():
    db_file_path=check_upload_file(form)
    selectedEvent.EventName=form.name.data
    selectedEvent.EventImage=db_file_path
    selectedEvent.EventGenre=form.genre.data
    selectedEvent.EventDescription=form.description.data
    selectedEvent.EventVenue=form.venue.data
    selectedEvent.EventStart=form.start.data
    selectedEvent.EventEnd=form.end.data
    selectedEvent.EventTickets=form.tickets.data
    selectedEvent.EventStatus=form.status.data
    db.session.commit()
    flash('Editted event')
    return redirect('/')
  elif request.method == 'GET':
    form.name.data = selectedEvent.EventName
    form.image.data = selectedEvent.EventImage
    form.genre.data = selectedEvent.EventGenre
    form.description.data = selectedEvent.EventDescription
    form.venue.data = selectedEvent.EventVenue
    form.start.data = selectedEvent.EventStart
    form.end.data = selectedEvent.EventEnd
    form.tickets.data = selectedEvent.EventTickets
    form.status.data = selectedEvent.EventStatus
  return render_template('events/edit.html', form=form)


@bp.route('/<event>/comment', methods = ['GET', 'POST']) 
def comment(event):  
    form = CommentForm()  
    #get the destination object associated to the page and the comment
    event_obj = MusicEvent.query.filter_by(id=event).first()  
    if form.validate_on_submit():  
      #read the comment from the form
      comment = Comment(text=form.text.data,  
                        events=event_obj, users=current_user) 
      #here the back-referencing works - comment.destination is set
      # and the link is created
      db.session.add(comment) 
      db.session.commit() 

      #flashing a message which needs to be handled by the html
      #flash('Your comment has been added', 'success')  
      print('Your comment has been added', 'success') 
    # using redirect sends a GET request to destination.show
    return redirect(url_for('event.show', id=event))

@bp.route('/book/<id>', methods=['GET','POST'])
@login_required
def book(id):
  event_obj = MusicEvent.query.filter_by(id=id).first()
  if (current_user.role == 'customer'):
    pass
  elif (current_user.role == 'admin'):
    return redirect('/Forbidden')
  else:
    return redirect('/Forbidden')
  
  print('Method type: ', request.method)
  form = OrderForm()
  if(form.validate_on_submit()):
    order = Order(
      quantity=form.quantity.data,  
      events=event_obj, 
      users=current_user)
    db.session.add(order)
    db.session.commit()
    flash('Event is booked')
    return redirect('/')
  return render_template('events/book.html', form=form)

@bp.route('/delete/<id>', methods=['GET'])
def delete(eid):
    selectedEvent = MusicEvent.query.filter_by(id=eid).first() ## Tells program to get the data from the customer selected ##
    db.session.delete(selectedEvent) ## Tells program to go to delete the selected customer details ##
    db.session.commit() ## Tells program to go to delete the selected customer details ##
    flash('Congratulations, you have deleted an Customer!')
    return redirect('/')

import os
from werkzeug.utils import secure_filename

  # a new function

  
def check_upload_file(form):
  fp=form.image.data
  filename=fp.filename
  BASE_PATH=os.path.dirname(__file__)

  upload_path=os.path.join(BASE_PATH,'static/images/event',secure_filename(filename))
  db_upload_path='/static/images/event/' + secure_filename(filename)
  fp.save(upload_path)
  return db_upload_path
