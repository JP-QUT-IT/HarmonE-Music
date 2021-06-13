## Import Necessary Modules ##
import re
from flask import ( 
    Blueprint, app, flash, render_template, request, url_for, redirect
)
from sqlalchemy.sql.schema import FetchedValue
from sqlalchemy.sql.sqltypes import Integer
from .models import MusicEvent, Comment, Order
from .forms import CommentForm, EventForm, EditEventForm, OrderForm
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import Integer
from flask_login import login_required, current_user
from . import db
import math

## Create a blueprint for events.py ##
bp = Blueprint('event', __name__, url_prefix='/events')

## Showing Event Function and Page Creation ##
@bp.route('/<id>') 
def show(id): 
  event = MusicEvent.query.filter_by(id=id).first()  
  cform = CommentForm()
  return render_template('events/show.html', event=event, form=cform)

## Creating Event Function and Page Creation ##
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


## Editing Event Function and Page Creation ##
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
    flash('Edited event')
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


## Comment Function and creation for selected Event ##
@bp.route('/<event>/comment', methods = ['GET', 'POST']) 
def comment(event):  
    form = CommentForm()  
    event_obj = MusicEvent.query.filter_by(id=event).first()  
    if form.validate_on_submit():  
      comment = Comment(
        text=form.text.data,  
        events=event_obj, 
        users=current_user) 
      db.session.add(comment) 
      db.session.commit()  
      flash('Your comment has been added', 'success') 
    return redirect(url_for('event.show', id=event))


## Booking Event Function and Page Creation ##
@bp.route('/book/<id>', methods = ['GET', 'POST']) 
@login_required
def book(event):  
    form = OrderForm() 
    if (current_user.role == 'customer'):
      pass
    elif (current_user.role == 'admin'):
      return redirect('/Forbidden')
    else:
      return redirect('/Forbidden') 
    event_obj = MusicEvent.query.filter_by(id=event).first()  
    if form.validate_on_submit():  
      order = Order(
        quantity=form.quantity.data,  
        events=event_obj, 
        users=current_user) 
      db.session.add(order) 
      db.session.commit() 

      flash('Your comment has been added', 'success') 

    return redirect(url_for('event.show', id=event))


## What the team wants the book page and function to do but doesn't work as there are errors with SQL data types and Python data types ##
# @bp.route('/book/<id>', methods = ['GET', 'POST']) 
# @login_required
# def book(id):

#   event_obj = MusicEvent.query.filter_by(id=id).first()
#   if (current_user.role == 'customer'):
#     pass
#   elif (current_user.role == 'admin'):
#     return redirect('/Forbidden')
#   else:
#     return redirect('/Forbidden')
  
#   print('Method type: ', request.method)
#   form = OrderForm()
#   if form.validate_on_submit():
#     selectedEvent = MusicEvent.query.filter_by(id = id).first()
#     order = Order(
#         quantity=form.quantity.data,  
#         events=event_obj, 
#         users=current_user)
#     db.session.add(order)
#     PurchaseQuantity = math.ceil(form.quantity)
#     if PurchaseQuantity > selectedEvent.EventTickets:
#       db.session.delete(order)
#     elif PurchaseQuantity < selectedEvent.EventTickets:
#       db.session.commit()
#     elif PurchaseQuantity == selectedEvent.EventTickets:
#       selectedEvent.EventTickets = '0'
#       selectedEvent.EventStatus = 'Booked Out'
#       db.session.commit() 
     
#     flash('Event is booked')
#     return redirect('/')
#   return render_template('events/book.html', form=form)


## A Delete Function that doesn't work ##
# @bp.route('/delete/<id>', methods=['GET'])
# def delete(id):
#     selectedEvent = MusicEvent.query.filter_by(id=id).first() ## Tells program to get the data from the customer selected ##
#     db.session.delete(selectedEvent) ## Tells program to go to delete the selected customer details ##
#     db.session.commit() ## Tells program to go to delete the selected customer details ##
#     flash('Congratulations, you have deleted an Customer!')
#     return redirect('/')


## File Upload Function ##
import os
from werkzeug.utils import secure_filename
def check_upload_file(form):
  fp=form.image.data
  filename=fp.filename
  BASE_PATH=os.path.dirname(__file__)

  upload_path=os.path.join(BASE_PATH,'static/images/event',secure_filename(filename))
  db_upload_path='/static/images/event/' + secure_filename(filename)
  fp.save(upload_path)
  return db_upload_path
