import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'INSERTaSUPERHardTOGue$TrinG!'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMIN_USER = os.environ.get('ADMIN_USER') or 'geek@geektechstuff.com'

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
         'sqlite:///' + os.path.join(basedir, 'data.sqlite')


class TestConfig(Config):
    TEST = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-TEST.sqlite')
    WTF_CSRF_ENABLED = False


config = {
    'production': ProdConfig,
    'default': ProdConfig,
    'test': TestConfig
}
