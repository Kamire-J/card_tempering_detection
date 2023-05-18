import os
from os import environ

class Config(object):
    DEBUG = False
    TESTING = False

    base_dir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = 'saboja'

    DB_NAME = 'production-db'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'saboja'

    UPLOADS = './static'

    SESSION_COOKIE_SECURE = True

    DEFAULT_THEME = None


class ProductionConfig(Config):
    pass 

class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = 'production-db'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'saboja'

    UPLOADS = './static'

    SESSION_COOKIE_SECURE = True



class TestingConfig(Config):
    DEBUG = True

    DB_NAME = 'production-db'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'saboja'

    UPLOADS = './static'

    SESSION_COOKIE_SECURE = True


class DebugConfig(Config):
    DEBUG = False


