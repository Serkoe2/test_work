from flask import Flask, session
from flask_cors import CORS
from importlib import import_module
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis


db = SQLAlchemy()
redis_client = FlaskRedis(decode_responses=True)

def register_extensions(app: Flask) -> None:
    """
    Регистрирует все расширения
    """
    CORS().init_app(app, resources={r"/*": {"origins": "*"}})
    db.init_app(app)
    redis_client.init_app(app)

def configure_database(app):

    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()

def register_blueprints(app: Flask) -> None:
    """
    Регистрирует все приложения
    """
    for module_name in ('rates',):
        module = import_module('apps.Api.{}'.format(module_name))
        app.register_blueprint(module.blueprint)
    
    for module_name in ('route',):
        module = import_module('apps.Pages.{}'.format(module_name))
        app.register_blueprint(module.blueprint)


def create_app(Config) -> Flask:
    """
    Создает и возвращает Flask приложение
    """
    app = Flask(__name__)
    app.config.from_object(Config)
    print(app.config)
    register_blueprints(app)
    register_extensions(app)
    configure_database(app)
    return app
