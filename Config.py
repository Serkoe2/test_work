import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    if not os.getenv("ENVIROMENT"):
        load_dotenv('.env')
    DEBUG = True
    SECRET_KEY = 'secret-key'
