from flask import Flask
from flask_cors import CORS
from importlib import import_module


def register_extensions(app: Flask) -> None:
    """
    Регистрирует все расширения
    """
    CORS().init_app(app, resources={r"/*": {"origins": "*"}})


def register_blueprints(app: Flask) -> None:
    """
    Регистрирует все приложения
    """
    for module_name in ('rates',):
        module = import_module('apps.Api.{}'.format(module_name))
        app.register_blueprint(module.blueprint)


def create_app(config: object) -> Flask:
    """
    Создает и возвращает Flask приложение
    """
    app = Flask(__name__)
    app.config.from_object(config)
    register_blueprints(app)
    register_extensions(app)
    return app
