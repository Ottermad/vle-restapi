"""Utils file."""
import requests
from flask_jwt_extended import get_jwt_identity


def forward_request_to_service(request, service, endpoint):
    """Forward incoming request to a Service and then returns the result."""
    url = "{}{}".format(service.host, endpoint)
    request_method = getattr(requests, request.method.lower())
    headers = dict(request.headers)

    current_identity = get_jwt_identity()
    if current_identity is not None:
        headers['User-Id'] = str(current_identity['id'])
        headers['School-Id'] = str(current_identity['school_id'])
        headers['Permissions'] = ",".join([p['name'] for p in current_identity['permissions']])

    params = request.args
    resp = request_method(url, params=params, json=request.json,
                          headers=headers)
    return resp.text, resp.status_code
