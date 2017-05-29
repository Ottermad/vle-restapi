"""Main Package."""
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import config
from services import Services

db = SQLAlchemy()
services = Services()
jwt = JWTManager()


def create_app(config_name="default"):
    """Create Flask object called app and return it."""
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    services.init_app(app)
    jwt.init_app(app)

    from .main.views import main_blueprint
    app.register_blueprint(main_blueprint)

    return app
