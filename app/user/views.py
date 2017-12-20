"""Views file."""
from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.utils import forward_request_to_service
from app import services


user_blueprint = Blueprint('user', __name__, url_prefix='/user')


@user_blueprint.route("/me")
@jwt_required
def me():
    return forward_request_to_service(request, services.user, "/user/me")


@user_blueprint.route("/user", methods=["GET", "POST"])
@jwt_required
def user_list_or_create():
    return forward_request_to_service(request, services.user, "/user/user")


@user_blueprint.route("/user/<int:user_id>", methods=["PUT", "GET", "DELETE"])
@jwt_required
def user_update_or_delete(user_id):
    return forward_request_to_service(
        request, services.user, "/user/user/{}".format(user_id))


permissions_blueprint = Blueprint('permission', __name__, url_prefix='/permissions')


@permissions_blueprint.route('/permission', methods=["POST", "GET"])
@jwt_required
def permission_listing_or_create_view():
    return forward_request_to_service(
        request, services.user, "/permissions/permission")


@permissions_blueprint.route('/permission/grant', methods=["POST", "DELETE"])
@jwt_required
def grant_or_remove_permission_view():
    return forward_request_to_service(
        request, services.user, "/permissions/permission/grant")


school_blueprint = Blueprint('school', __name__, url_prefix='/school')


@school_blueprint.route("/signup", methods=("POST",))
def signup():
    return forward_request_to_service(request, services.user, "/school/signup")
