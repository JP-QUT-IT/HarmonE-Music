from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db=SQLAlchemy()

#404 not found error handling
def page_not_found(e):
    return render_template('Error_Handling/404.html'), 404

#500 internal server error error handling
def internal_server_error(e):
    return render_template('Error_Handling/500.html'), 500

def create_app():
  
    app=Flask(__name__)
    app.debug=True
    app.secret_key='utroutoru'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///MusicEvent.sqlite'
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)
    db.init_app(app)

    bootstrap = Bootstrap(app)
    UPLOAD_FOLDER = '/images/'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    login_manager = LoginManager()
    login_manager.login_view='auth.login'  
    login_manager.init_app(app)

    from .models import User
    @login_manager.user_loader  
    def load_user(user_id):
        return User.query.get(int(user_id))


    from . import views
    app.register_blueprint(views.mainbp)

    from . import events
    app.register_blueprint(events.bp)

    from . import auth
    app.register_blueprint(auth.bp)
    
    return app
