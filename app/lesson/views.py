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
