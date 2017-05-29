"""Views file."""
import requests

from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required

from internal.exceptions import HTTPException, MissingKeyError, NoJSONError

from app.utils import forward_request_to_service
from app import services


user_blueprint = Blueprint('user', __name__, url_prefix='/user')

@user_blueprint.route("/auth", methods=("POST",))
def create_token():
    """Route to create a JWT token."""
    json_data = request.get_json()
    if json_data is None:
        raise NoJSONError()

    expected_keys = ["username", "password"]
    for key in expected_keys:
        if key not in json_data.keys():
            raise MissingKeyError(key)

    username = json_data['email']
    password = json_data['password']

    # Check email and password
    response = services.user.post(
        'authenticate',
        json={'username': username, 'password': password},
        headers={'Content-Type': 'application/json'}
    )

    if response.status_code != 200:
        raise HTTPException(
            response.status_code,
            response.json()
        )

    user_id = response.json()['id']
    token = {'access_token': create_access_token(identity=user_id), 'user_id': user_id}

    return jsonify(token)
