from flask_restx import Resource, fields
from flask import request, jsonify
from libs.shared.data_transfer import UserCreateDTO
from libs.server.services import UserService
from apps.flask_api.middleware import generate_jwt, require_admin
from libs.server.data_access.model import ApiKey
from libs.server.data_access.database import db
from . import api

# Define API models
user_model = api.model(
    "User",
    {"name": fields.String(required=True), "email": fields.String(required=True)},
)


# Define routes
@api.route("/users")
class UserResource(Resource):
    @api.expect(user_model)
    def post(self):
        data = api.payload
        user_dto = UserCreateDTO(**data)
        user = UserService.create_user(user_dto)
        return {"id": user.id, "name": user.name, "email": user.email}, 201


@api.route("/generate_key")
class GenerateKeyResource(Resource):
    @require_admin
    def post(self):
        data = request.json
        is_admin = data.get("is_admin", False)
        duration = (
            None if is_admin else 30
        )  # Admin keys never expire; User keys expire in 30 days

        api_key = ApiKey.generate_key(is_admin=is_admin, duration=duration)
        db.session.add(api_key)
        db.session.commit()

        token = generate_jwt(api_key.key, is_admin)
        return jsonify({"api_key": api_key.key, "jwt": token})


@api.route("/health", methods=["GET"])
class HealthCheck(Resource):
    def get(self):
        return {"status": "healthy"}, 200
