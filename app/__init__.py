"""Main Package."""
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import config
from services import Services
from internal.exceptions import CustomError

db = SQLAlchemy()
services = Services()
jwt = JWTManager()


def create_app(config_name="default"):
    """Create Flask object called app and return it."""
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    @app.errorhandler(CustomError)
    def custom_error(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    db.init_app(app)
    services.init_app(app)
    jwt.init_app(app)

    from .main.views import main_blueprint
    app.register_blueprint(main_blueprint)

    from .user.views import (
        user_blueprint, permissions_blueprint, school_blueprint
    )
    app.register_blueprint(user_blueprint)
    app.register_blueprint(permissions_blueprint)
    app.register_blueprint(school_blueprint)

    return app
