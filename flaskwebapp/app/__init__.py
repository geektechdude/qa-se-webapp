from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.logon'


def create_app(config_name):
    # Creates and configures the app
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # initialise Bootstrap
    bootstrap.init_app(app)

    # initialise Database
    db.init_app(app)

    # initialise Login Manager
    login_manager.init_app(app)

    # imports main views.py blueprints and sets endpoints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # imports auth views.py blueprints and sets endpoints
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
