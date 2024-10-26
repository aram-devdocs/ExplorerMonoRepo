from flask import Blueprint
from flask_restx import Api

# Initialize the blueprint and API
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Import and register individual route modules
from .route import *  # Import all routes to register them with the API