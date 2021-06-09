import re
from flask import ( 
    Blueprint, app, flash, render_template, request, url_for, redirect
) 
from .models import MusicEvent, Comment, Customer, Administrator, Status
from .forms import CommentForm, EventForm, EditEventForm
from flask_login import login_required, current_user
from . import db

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
  print('Method type: ', request.method)
  form = EventForm()
  if(form.validate_on_submit()):
    db_file_path=check_upload_file(form)
    event=MusicEvent(
      EventName=form.name.data, 
      EventCreator=current_user, 
      EventImage=db_file_path,
      EventDescription=form.description.data,
      EventVenue=form.venue.data,
      EventStart=form.start.data,
      EventEnd=form.end.data,
      EventTickets=form.tickets.data,
      EventStatus=form.status.data)
    
    db.session.add(event)
    db.session.commit()
    return redirect('/events')
  return render_template('events/create.html', form=form)

@bp.route('/edit/<id>', methods=['GET', 'POST'])
@login_required
def edit(id):
  selectedEvent = MusicEvent.query.filter_by(id = id).first()
  form = EditEventForm(name=selectedEvent)
  if form.validate_on_submit():
    db_file_path=check_upload_file(form)
    selectedEvent.EventName=form.name.data
    selectedEvent.EventImage=db_file_path
    selectedEvent.EventDescription=form.description.data
    selectedEvent.EventVenue=form.venue.data
    selectedEvent.EventStart=form.start.data
    selectedEvent.EventEnd=form.end.data
    selectedEvent.EventTickets=form.tickets.data
    selectedEvent.EventStatus=form.status.data
    db.session.commit()
    flash('Editted')
    return redirect('/')
  elif request.method == 'GET':
    form.name.data = selectedEvent.EventName
    form.image.data = selectedEvent.EventImage
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
                        event=event_obj, customer=current_user) 
      #here the back-referencing works - comment.destination is set
      # and the link is created
      db.session.add(comment) 
      db.session.commit() 

      #flashing a message which needs to be handled by the html
      #flash('Your comment has been added', 'success')  
      print('Your comment has been added', 'success') 
    # using redirect sends a GET request to destination.show
    return redirect(url_for('event.show', id=event))

import os
from werkzeug.utils import secure_filename

  # a new function
def check_upload_file(form):
  fp=form.image.data
  filename=fp.filename
  BASE_PATH=os.path.dirname(__file__)

  upload_path=os.path.join(BASE_PATH,'static/image',secure_filename(filename))
  db_upload_path='/static/image/' + secure_filename(filename)
  fp.save(upload_path)
  return db_upload_path
