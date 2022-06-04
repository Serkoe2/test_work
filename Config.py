import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    if not os.getenv("ENVIROMENT"):
        load_dotenv('.env')
    Environment  = 'development'
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'secret-key'
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'migrations')
