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

    # imports views.py blueprints and sets endpoints
    from .main import views
    app.register_blueprint(views.bp)
    app.add_url_rule('/', endpoint='index')

    return app