import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    Environment  = 'development'
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'secret-key'
    ENV = 'development'
