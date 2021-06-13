## Import Necessary Modules ##
from flask import ( 
    Blueprint, flash, render_template, request, url_for, redirect
) 
from werkzeug.security import generate_password_hash,check_password_hash
from .models import User
from .forms import LoginForm, RegisterForm
from flask_login import login_user, login_required, logout_user
from . import db


## Create a blueprint for auth.py ##
bp = Blueprint('auth', __name__)


## Login Function and Page ##
@bp.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    error=None
    if(login_form.validate_on_submit()==True):
        username = login_form.username.data
        password = login_form.password.data
        u1 = User.query.filter_by(name=username).first()
        if u1 is None:
            error='Incorrect user name'
        elif not check_password_hash(u1.password_hash, password): # takes the hash and password
            error='Incorrect password'
        if error is None:
            login_user(u1)
            return redirect(url_for('main.index'))
        else:
            flash(error)
    return render_template('user.html', form=login_form, heading='Login')

## Register Function and Page ##
@bp.route('/register', methods=['GET','POST'])
def register():
    register = RegisterForm()
    if (register.validate_on_submit() == True):
            uname =register.username.data
            pwd = register.password.data
            email=register.email.data
            contact=register.contact_number.data
            addresss=register.address.data
            role = register.usertype.data
            u1 = User.query.filter_by(name=uname).first()
            if u1:
                flash('User name already exists, please login')
                return redirect(url_for('auth.login'))
            pwd_hash = generate_password_hash(pwd)
            new_cust = User(name=uname, password_hash=pwd_hash, emailid=email, contactnumber=contact, addres=addresss, role=role)
            db.session.add(new_cust)
            db.session.commit()
            return redirect(url_for('main.index'))
    else:
        return render_template('user.html', form=register, heading='Register')


## Logout Function ##
@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))