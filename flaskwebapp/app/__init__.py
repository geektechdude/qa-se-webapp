from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name):
    # Creates and configures the app
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # initialise Database
    db.init_app(app)

    # imports main views.py blueprints and sets endpoints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # imports auth views.py blueprints and sets endpoints
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app