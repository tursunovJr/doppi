from flask import Blueprint, json
from flask_restful import Api
from werkzeug.exceptions import HTTPException


api_bp = Blueprint("api", __name__)
api = Api(api_bp)

# Add resources

# Auth API Module

# JSON format for error
@api_bp.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response
