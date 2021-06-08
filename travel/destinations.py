import re
from flask import ( 
    Blueprint, app, flash, render_template, request, url_for, redirect
) 
from .models import Destination,Comment,Customer
from .forms import CommentForm, DestinationForm, EditDestinationForm
from flask_login import login_required, current_user
from . import db

#create a blueprint
bp = Blueprint('destination', __name__, url_prefix='/destinations')

#create a page that will show the details fo the destination
@bp.route('/<id>') 
def show(id): 
  destination = Destination.query.filter_by(id=id).first()  
  cform = CommentForm()
  return render_template('destinations/show.html', destination=destination, form=cform)


@bp.route('/create', methods=['GET','POST'])
@login_required
def create():
  print('Method type: ', request.method)
  form = DestinationForm()
  if(form.validate_on_submit()):
    db_file_path=check_upload_file(form)
    destination=Destination(name=form.name.data,description=form.description.data, 
    image=db_file_path,currency=form.currency.data)
    
    db.session.add(destination)
    db.session.commit()
    return redirect('/destinations')
  return render_template('destinations/create.html', form=form)

@bp.route('/edit/<id>', methods=['GET', 'POST'])
@login_required
def edit(id):
  selectedDestination = Destination.query.filter_by(id = id).first()
  form = EditDestinationForm(name=selectedDestination)
  if form.validate_on_submit():
    db_file_path=check_upload_file(form)
    selectedDestination.name = form.name.data
    selectedDestination.description = form.description.data
    selectedDestination.image = db_file_path
    selectedDestination.currency = form.currency.data
    db.session.commit()
    flash('Editted')
    return redirect('/')
  elif request.method == 'GET':
    form.name.data = selectedDestination.name
    form.description.data = selectedDestination.description
    form.image.data = selectedDestination.image
    form.currency.data = selectedDestination.currency
  return render_template('destinations/edit.html', form=form)


@bp.route('/<destination>/comment', methods = ['GET', 'POST'])  
def comment(destination):  
    form = CommentForm()  
    #get the destination object associated to the page and the comment
    destination_obj = Destination.query.filter_by(id=destination).first()  
    if form.validate_on_submit():  
      #read the comment from the form
      comment = Comment(text=form.text.data,  
                        destination=destination_obj, customer=current_user) 
      #here the back-referencing works - comment.destination is set
      # and the link is created
      db.session.add(comment) 
      db.session.commit() 

      #flashing a message which needs to be handled by the html
      #flash('Your comment has been added', 'success')  
      print('Your comment has been added', 'success') 
    # using redirect sends a GET request to destination.show
    return redirect(url_for('destination.show', id=destination))

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
