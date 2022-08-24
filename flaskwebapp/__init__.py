import flask
import os

def create_app(test_config=None):
    # Creates and configures the app
    app = flask.Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='DEV',
        DATABASE=os.path.join(app.instance_path,'webapp.sqlite')
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # imports test.py blueprints and sets endpoints
    from . import views
    app.register_blueprint(views.bp)
    app.add_url_rule('/', endpoint='index')

    # imports database commands / connection
    from . import database
    database.init_app(app)

    # imports auth (login) blueprint
    from . import auth
    app.register_blueprint(auth.bp)

    return app