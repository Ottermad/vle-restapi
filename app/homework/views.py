from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.utils import forward_request_to_service
from app import services


homework_blueprint = Blueprint('homework', __name__, url_prefix='/homework')


@homework_blueprint.route('/submissions')
@jwt_required
def submissions():
    return forward_request_to_service(request, services.homework, "/homework/submissions")


@homework_blueprint.route('/homework/<int:homework_id>/submissions')
@jwt_required
def homework_submissions(homework_id):
    return forward_request_to_service(
        request, services.homework, "/homework/homework/{}/submissions".format(homework_id))


@homework_blueprint.route('/summary', methods=['POST', 'GET'])
@jwt_required
def summary():
    return forward_request_to_service(request, services.homework, "/homework/summary")


@homework_blueprint.route('/due/<int:homework_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required
def due(homework_id):
    return forward_request_to_service(request, services.homework, "/homework/due/{}".format(homework_id))


@homework_blueprint.route('/quiz', methods=("POST", "GET"))
@jwt_required
def quiz_create():
    return forward_request_to_service(
        request, services.homework, '/quiz/')


@homework_blueprint.route('/quiz/<int:quiz_id>', methods=("POST", "GET"))
@jwt_required
def quiz_detail_or_submit(quiz_id):
    return forward_request_to_service(
        request, services.homework, '/quiz/{}'.format(quiz_id))


@homework_blueprint.route('/quiz/submission/<int:submission_id>')
@jwt_required
def quiz_submissions(submission_id):
    return forward_request_to_service(
        request, services.homework, '/quiz/submission/{}'.format(submission_id))


@homework_blueprint.route('/essay', methods=("POST", "GET"))
@jwt_required
def essay_create():
    return forward_request_to_service(
        request, services.homework, '/essay/')


@homework_blueprint.route('/essay/<int:essay_id>', methods=("POST", "GET"))
@jwt_required
def essay_detail_or_submit(essay_id):
    return forward_request_to_service(
        request, services.homework, '/essay/{}'.format(essay_id))


@homework_blueprint.route('/essay/submission/<int:submission_id>')
@jwt_required
def essay_submissions(submission_id):
    return forward_request_to_service(
        request, services.homework, '/essay/submission/{}'.format(submission_id))
