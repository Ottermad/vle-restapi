"""Views file."""
from flask import Blueprint, jsonify, request

from flask_jwt_extended import create_access_token

from internal.exceptions import MissingKeyError, NoJSONError, CustomError

from app import services

from .models import *

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route("/")
def index():
    return "Index"


@main_blueprint.route("/auth", methods=("POST",))
def create_token():
    """Route to create a JWT token."""
    json_data = request.get_json()
    if json_data is None:
        raise NoJSONError()

    expected_keys = ["username", "password"]
    for key in expected_keys:
        if key not in json_data.keys():
            raise MissingKeyError(key)

    username = json_data['username']
    password = json_data['password']

    # Check email and password
    response = services.user.post(
        'user/authenticate',
        json={'username': username, 'password': password},
        headers={'Content-Type': 'application/json'}
    )

    if response.status_code != 200:
        raise CustomError(
            **response.json()
        )

    user_id = response.json()['user']['id']
    token = {'access_token': create_access_token(identity=response.json()['user']), 'user_id': user_id}

    return jsonify(token)
