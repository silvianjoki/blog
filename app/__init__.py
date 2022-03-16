from flask import Flask
import os
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES



# initializing bootstrap extension
bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
photos = UploadSet('photos',IMAGES)


def create_app(config_name):
    app = Flask(__name__)
    
    # , send_from_directory
    # @app.route("/static/<path:path>")
    # def static_dir(path):
    #     return send_from_directory("static", path)


    # creating app configurations
    app.config.from_object(config_options[config_name])
    
    # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.ge("DATABASE_URL")
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    # initalizing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    # configure UploadSet
    configure_uploads(app,photos)
    
    # Registering the blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    #...
    from .auth import auth as auth_blueprint 
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
    
    return app