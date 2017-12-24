"""Views file."""
from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.utils import forward_request_to_service
from app import services


lesson_blueprint = Blueprint('lesson', __name__, url_prefix='/lessons')


@lesson_blueprint.route('/subject', methods=['POST', 'GET'])
@jwt_required
def subject_list_or_create_view():
    return forward_request_to_service(request, services.lesson, "/subject/subject")


@lesson_blueprint.route('/subject/<id>', methods=['PUT', 'GET', 'DELETE'])
@jwt_required
def subject_detail_delete_update(id):
    return forward_request_to_service(
        request, services.lesson, "/subject/subject/{}".format(id))


@lesson_blueprint.route('/lesson', methods=['POST', 'GET'])
@jwt_required
def lesson_list_or_create_view():
    return forward_request_to_service(request, services.lesson, "/lessons/lesson")


@lesson_blueprint.route('/lesson/<int:lesson_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required
def lesson_detail_view(lesson_id):
    return forward_request_to_service(request, services.lesson, "/lessons/lesson/{}".format(lesson_id))


@lesson_blueprint.route('/lesson/taught')
@jwt_required
def lesson_taught():
    return forward_request_to_service(
        request, services.lesson, '/lessons/lesson/taught')
